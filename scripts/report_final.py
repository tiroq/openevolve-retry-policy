import os
import re
import json
import difflib
from pathlib import Path

LOG_FILE = 'openevolve_output/logs/openevolve_20260421_110550.log'
OUTPUT_DIR = Path('openevolve_output')
INITIAL_PROGRAM = 'initial_program.py'
REPORT_PATH = Path('docs/evolution_progress_detailed.md')

def extract_evolve_block(code):
    pattern = r'### EVOLVE-BLOCK-START ###(.*?)### EVOLVE-BLOCK-END ###'
    match = re.search(pattern, code, re.DOTALL)
    return match.group(1).strip() if match else code.strip()

def get_program_code(prog_id):
    if prog_id == '61b091ad-3607-471b-acdd-ae0f6c285c27' and os.path.exists(INITIAL_PROGRAM):
        return open(INITIAL_PROGRAM).read()
    for f in OUTPUT_DIR.glob('checkpoints/**/programs/*.json'):
        if prog_id in f.name:
            return json.load(open(f)).get('code', '')
    return ''

def parse_metrics(line):
    parts = line.split('Metrics:')[1].split(',')
    m = {}
    for p in parts:
        if '=' in p:
            k, v = p.split('=')
            m[k.strip()] = float(v.strip())
    return m

iterations, transitions, current_best_id = [], [], '61b091ad-3607-471b-acdd-ae0f6c285c27'
if os.path.exists(LOG_FILE):
    lines = open(LOG_FILE).readlines()
    for i, line in enumerate(lines):
        m = re.search(r'Iteration (\d+): Program ([a-f0-9-]+).*completed in ([\d.]+)s', line)
        if m:
            iter_id = int(m.group(1))
            prog_id = m.group(2)
            dur = m.group(3)
            metrics = {}
            # Metrics are usually on the same timestamp or next line
            if i+1 < len(lines) and 'Metrics:' in lines[i+1]:
                metrics = parse_metrics(lines[i+1])
            elif 'Metrics:' in line:
                metrics = parse_metrics(line)
            
            iterations.append({'id': iter_id, 'prog': prog_id, 'm': metrics, 'dur': dur})
            
            if i+2 < len(lines) and 'New best solution found!' in lines[i+2]:
                transitions.append({'from': current_best_id, 'to': prog_id, 'iter': iter_id, 'm': metrics.copy()})
                current_best_id = prog_id

md = [f'# Evolution Detailed Report\nSource: `{LOG_FILE}`', '\n## Detailed Metrics']
md.append('| Iter | Result | Score | Success | Latency | Retries | Dur |')
md.append('|---|---|---|---|---|---|---|')
for it in iterations:
    m = it['m']
    md.append(f'| {it["id"]} | {it["prog"][:8]} | {m.get("combined_score",0):.2f} | {m.get("success_rate",0):.2f} | {m.get("avg_latency_ms",0):.1f} | {m.get("avg_retry_count",0):.1f} | {it["dur"]}s |')

md.append('\n## Best Solution Evolution')
for bt in transitions:
    md.append(f'### Iteration {bt["iter"]} (New Best: {bt["to"][:8]})')
    md.append(f'**Score:** {bt["m"].get("combined_score",0):.2f}')
    c1, c2 = get_program_code(bt['from']), get_program_code(bt['to'])
    if c1 and c2:
        diff = list(difflib.unified_diff(extract_evolve_block(c1).splitlines(), extract_evolve_block(c2).splitlines(), lineterm=''))
        md.extend(['\n```diff', *diff, '```'])

with open(REPORT_PATH, 'w') as f:
    f.write('\n'.join(md))
