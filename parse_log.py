import re
import sys

log_path = 'openevolve_output/logs/openevolve_20260421_110550.log'
try:
    with open(log_path, 'r') as f:
        content = f.read()
except FileNotFoundError:
    print(f"File {log_path} not found")
    sys.exit(1)

print('### 1) Iterations and Metrics Table')
print('| iteration | program_id | parent_id | duration_s | combined_score | success_rate | avg_latency_ms | avg_retry_count | useless_retries | good_endpoint_switches |')
print('|---|---|---|---|---|---|---|---|---|---|')

pattern = r"Iteration (\d+): Program ([a-f0-9-]+) \(parent: ([a-f0-9-]+)\) completed in ([\d.]+)s[\s\S]*?Metrics: (.*?)\n"
iter_blocks = re.findall(pattern, content)

for it, pid, parent, dur, metrics_str in iter_blocks:
    metrics = {}
    for entry in metrics_str.split(','):
        if '=' in entry:
            k, v = entry.split('=')
            metrics[k.strip()] = v.strip()
    
    row = [
        it, pid, parent, dur,
        metrics.get('combined_score', ''),
        metrics.get('success_rate', ''),
        metrics.get('avg_latency_ms', ''),
        metrics.get('avg_retry_count', ''),
        metrics.get('useless_retries', ''),
        metrics.get('good_endpoint_switches', '')
    ]
    print('| ' + ' | '.join(row) + ' |')

print('\n### 2) Checkpoint Saves')
# 2026-04-21 11:07:15,017 - openevolve.controller - INFO - Saved checkpoint at iteration 5 to openevolve_output/checkpoints/checkpoint_5
checkpoints = re.findall(r'Saved checkpoint at iteration (\d+) to (.*)', content)
# Use a set to handle duplicates
seen_checkpoints = set()
for it, path in checkpoints:
    if (it, path) not in seen_checkpoints:
        print(f'{it}: {path}')
        seen_checkpoints.add((it, path))

print('\n### 3) New Best Programs')
# 🌟 New best solution found at iteration 1: 57e93334-be2b-455c-b98e-8bc43b90c6b7
bests = re.findall(r'New best solution found at iteration (\d+): ([a-f0-9-]+)', content)
for it, pid in bests:
    score = "N/A"
    for b_it, b_pid, b_parent, b_dur, b_metrics_str in iter_blocks:
        if b_it == it and b_pid == pid:
            for entry in b_metrics_str.split(','):
                if 'combined_score' in entry:
                    score = entry.split('=')[1].strip()
                    break
            break
    print(f'Iteration {it}: score {score}')
