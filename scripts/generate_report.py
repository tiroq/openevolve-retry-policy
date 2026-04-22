#!/usr/bin/env python3
"""Generate a detailed evolution-progress report from an OpenEvolve run.

Usage:
    # Auto-detect the latest log in openevolve_output/logs/
    python scripts/generate_report.py

    # Explicit log file
    python scripts/generate_report.py --log openevolve_output/logs/openevolve_20260422_103145.log

    # Custom output path
    python scripts/generate_report.py --output docs/my_report.md

    # Different output root (if OpenEvolve was run with a custom --output-dir)
    python scripts/generate_report.py --output-dir path/to/openevolve_output
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# ── constants ────────────────────────────────────────────────────────────────

METRICS: List[str] = [
    "runs_successfully",
    "success_rate",
    "avg_latency_ms",
    "avg_retry_count",
    "dangerous_non_idempotent_retries",
    "useless_retries",
    "good_fail_fast_decisions",
    "good_endpoint_switches",
    "combined_score",
]

# ── data classes ──────────────────────────────────────────────────────────────


class IterationRecord:
    __slots__ = ("iteration", "program_id", "parent_id", "metrics", "duration_s", "is_new_best")

    def __init__(
        self,
        iteration: int,
        program_id: str,
        parent_id: str,
        metrics: Dict[str, float],
        duration_s: float,
    ) -> None:
        self.iteration = iteration
        self.program_id = program_id
        self.parent_id = parent_id
        self.metrics = metrics
        self.duration_s = duration_s
        self.is_new_best = False


class NewBestEvent:
    __slots__ = ("iteration", "old_id", "new_id", "old_score", "new_score", "delta")

    def __init__(
        self,
        iteration: int,
        old_id: str,
        new_id: str,
        old_score: float,
        new_score: float,
        delta: float,
    ) -> None:
        self.iteration = iteration
        self.old_id = old_id
        self.new_id = new_id
        self.old_score = old_score
        self.new_score = new_score
        self.delta = delta


class CheckpointRecord:
    __slots__ = ("checkpoint", "n_programs", "best_score", "best_id")

    def __init__(
        self, checkpoint: int, n_programs: int, best_score: float, best_id: str
    ) -> None:
        self.checkpoint = checkpoint
        self.n_programs = n_programs
        self.best_score = best_score
        self.best_id = best_id


# ── helpers ───────────────────────────────────────────────────────────────────


def parse_metrics_str(text: str) -> Dict[str, float]:
    """Extract metric key=value pairs from a log-line fragment."""
    result: Dict[str, float] = {}
    for metric in METRICS:
        match = re.search(rf"{metric}=(-?[\d.]+(?:e[+-]?\d+)?)", text)
        if match:
            result[metric] = float(match.group(1))
    return result


def extract_evolve_block(code: str) -> str:
    """Return only the lines between EVOLVE-BLOCK-START and EVOLVE-BLOCK-END (inclusive)."""
    start_marker = "# EVOLVE-BLOCK-START"
    end_marker = "# EVOLVE-BLOCK-END"
    if start_marker in code and end_marker in code:
        s = code.index(start_marker)
        e = code.index(end_marker) + len(end_marker)
        return code[s:e]
    return code


def find_program_json(program_id: str, output_dir: Path) -> Optional[Path]:
    """Search all checkpoint program directories for a JSON file matching program_id."""
    for path in sorted(output_dir.glob("checkpoints/checkpoint_*/programs/*.json")):
        if path.stem == program_id:
            return path
    return None


def read_program_code(program_id: str, output_dir: Path) -> Optional[str]:
    """Return the `code` field from a checkpoint program JSON, or None if not found."""
    path = find_program_json(program_id, output_dir)
    if path is None:
        return None
    data = json.loads(path.read_text())
    return data.get("code")


def unified_diff_blocks(
    old_code: str,
    new_code: str,
    old_label: str,
    new_label: str,
) -> str:
    """Return a unified diff of the EVOLVE-BLOCK between two full program strings."""
    old_lines = extract_evolve_block(old_code).splitlines(keepends=True)
    new_lines = extract_evolve_block(new_code).splitlines(keepends=True)
    return "".join(difflib.unified_diff(old_lines, new_lines, fromfile=old_label, tofile=new_label))


def fmt(value: float, precision: int = 4) -> str:
    """Format a float for table display, handling NaN and very large magnitudes."""
    if value != value:  # NaN check
        return "N/A"
    if abs(value) >= 1e8:
        return f"{value:.2e}"
    return f"{value:.{precision}f}"


def run_evaluator(
    program_path: Path,
    dataset: str,
    evaluator_path: Path,
    python_exe: str,
) -> Dict[str, float]:
    """Run `evaluator.py --program <path> --dataset <dataset> --json` and parse output.

    Returns an empty dict on any failure.
    """
    try:
        result = subprocess.run(
            [python_exe, str(evaluator_path), "--program", str(program_path), "--dataset", dataset, "--json"],
            capture_output=True,
            text=True,
            timeout=120,
        )
        if result.returncode != 0:
            print(
                f"  WARNING: evaluator returned exit {result.returncode} for "
                f"{program_path.name}/{dataset}: {result.stderr.strip()[:200]}",
                file=sys.stderr,
            )
            return {}
        return json.loads(result.stdout)
    except Exception as exc:  # noqa: BLE001
        print(f"  WARNING: could not evaluate {program_path.name}/{dataset}: {exc}", file=sys.stderr)
        return {}


# ── log parsing ───────────────────────────────────────────────────────────────

# Compiled patterns (module-level for reuse)
_ITER_PAT = re.compile(
    r"Iteration (\d+): Program ([0-9a-f-]+) \(parent: ([0-9a-f-]+)\) completed in ([\d.]+)s"
)
_METRICS_PAT = re.compile(r"Metrics: (.+)$")
_NEW_BEST_PAT = re.compile(
    r"- INFO - New best program ([0-9a-f-]+) replaces ([0-9a-f-]+)"
    r" \(combined_score: (-?[\d.e+-]+) → (-?[\d.e+-]+), ([+-][\d.e+-]+)\)"
)
_CK_PROGRAMS_PAT = re.compile(
    r"Saved database with (\d+) programs to .+checkpoint_(\d+)"
)
_CK_BEST_PAT = re.compile(
    r"Saved best program at checkpoint (\d+) with metrics: (.+)$"
)
_CK_SAVED_PAT = re.compile(r"Saved checkpoint at iteration (\d+)")
_ISLAND_PAT = re.compile(
    r"Island \d+: \d+ programs, best=(-?[\d.e+-]+).+\(best: ([0-9a-f-]+)\)"
)
_INIT_EVAL_PAT = re.compile(r"Evaluated program ([0-9a-f-]+) in [\d.]+s: (.+)$")
_MODEL_PAT = re.compile(r"Initialized OpenAI LLM with model: (.+)$")
_SEED_PAT = re.compile(r"Set random seed to (\d+)")
_TS_PAT = re.compile(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})")


def parse_log(
    log_path: Path,
) -> Tuple[
    List[IterationRecord],
    List[NewBestEvent],
    List[CheckpointRecord],
    Dict[str, str],
    Optional[str],
    Dict[str, float],
]:
    """Parse an OpenEvolve log file.

    Returns:
        iterations:      one record per completed iteration
        new_bests:       one record per new-best event
        checkpoints:     one record per saved checkpoint
        meta:            {start_time, end_time, model, seed}
        init_program_id: UUID of the initial (seed) program
        init_metrics:    metrics dict for the seed program
    """
    lines = log_path.read_text().splitlines()

    iterations: List[IterationRecord] = []
    new_bests: List[NewBestEvent] = []
    meta: Dict[str, str] = {}

    checkpoint_programs: Dict[int, int] = {}
    checkpoint_best_metrics: Dict[int, Dict[str, float]] = {}
    checkpoint_best_id: Dict[int, str] = {}

    init_program_id: Optional[str] = None
    init_metrics: Dict[str, float] = {}

    pending_iter: Optional[IterationRecord] = None
    last_island_best_id: Optional[str] = None

    for line in lines:
        # Start timestamp (first occurrence only)
        if "start_time" not in meta:
            ts_m = _TS_PAT.match(line)
            if ts_m:
                meta["start_time"] = ts_m.group(1)

        # Model name
        m = _MODEL_PAT.search(line)
        if m:
            meta["model"] = m.group(1)

        # Random seed
        m = _SEED_PAT.search(line)
        if m:
            meta["seed"] = m.group(1)

        # Initial program evaluation (happens before any iteration)
        if not iterations and not pending_iter:
            m = _INIT_EVAL_PAT.search(line)
            if m and not init_program_id:
                init_program_id = m.group(1)
                init_metrics = parse_metrics_str(m.group(2))

        # New-best event (appears before the matching iteration completion line)
        m = _NEW_BEST_PAT.search(line)
        if m:
            new_id = m.group(1)
            old_id = m.group(2)
            old_score = float(m.group(3))
            new_score = float(m.group(4))
            delta = float(m.group(5))
            new_bests.append(
                NewBestEvent(-1, old_id, new_id, old_score, new_score, delta)
            )

        # Iteration completion line
        m = _ITER_PAT.search(line)
        if m:
            pending_iter = IterationRecord(
                iteration=int(m.group(1)),
                program_id=m.group(2),
                parent_id=m.group(3),
                metrics={},
                duration_s=float(m.group(4)),
            )

        # Metrics line (immediately follows the iteration completion line)
        m = _METRICS_PAT.search(line)
        if m and pending_iter is not None:
            pending_iter.metrics = parse_metrics_str(m.group(1))
            # Link to any pending new-best event for this program
            for nb in new_bests:
                if nb.new_id == pending_iter.program_id and nb.iteration == -1:
                    nb.iteration = pending_iter.iteration
                    pending_iter.is_new_best = True
            iterations.append(pending_iter)
            pending_iter = None

        # Island status line (last one seen before a checkpoint save = best at that checkpoint)
        m = _ISLAND_PAT.search(line)
        if m:
            last_island_best_id = m.group(2)

        # Checkpoint: program count
        m = _CK_PROGRAMS_PAT.search(line)
        if m:
            checkpoint_programs[int(m.group(2))] = int(m.group(1))

        # Checkpoint: best metrics at save time
        m = _CK_BEST_PAT.search(line)
        if m:
            ck = int(m.group(1))
            checkpoint_best_metrics[ck] = parse_metrics_str(m.group(2))

        # Checkpoint: save confirmation (record last known island best as the checkpoint best)
        m = _CK_SAVED_PAT.search(line)
        if m:
            ck = int(m.group(1))
            if last_island_best_id:
                checkpoint_best_id[ck] = last_island_best_id

    # Build sorted checkpoint list
    all_checkpoints = sorted(
        set(checkpoint_programs) | set(checkpoint_best_metrics)
    )
    checkpoints: List[CheckpointRecord] = []
    for ck in all_checkpoints:
        mets = checkpoint_best_metrics.get(ck, {})
        checkpoints.append(
            CheckpointRecord(
                checkpoint=ck,
                n_programs=checkpoint_programs.get(ck, 0),
                best_score=mets.get("combined_score", float("nan")),
                best_id=checkpoint_best_id.get(ck, "unknown"),
            )
        )

    # End timestamp: last timestamp found in the log
    for line in reversed(lines):
        ts_m = _TS_PAT.match(line)
        if ts_m:
            meta["end_time"] = ts_m.group(1)
            break

    return iterations, new_bests, checkpoints, meta, init_program_id, init_metrics


# ── report generation ─────────────────────────────────────────────────────────


def generate_report(
    log_path: Path,
    output_dir: Path,
    initial_program_path: Path,
    evaluator_path: Path | None = None,
    python_exe: str = sys.executable,
) -> str:
    iterations, new_bests, checkpoints, meta, init_id, init_metrics = parse_log(log_path)
    init_code = initial_program_path.read_text()

    # --- Read final best info ---
    final_best_json = output_dir / "best" / "best_program_info.json"
    final_best_id: Optional[str] = None
    final_best_metrics: Dict[str, float] = {}
    if final_best_json.exists():
        fb_data = json.loads(final_best_json.read_text())
        final_best_id = fb_data.get("id")
        # metrics may be stored as a dict of {name: value} or {name: {value: ...}}
        raw_metrics = fb_data.get("metrics", {})
        if raw_metrics:
            # Normalise: some OpenEvolve versions store metrics as {key: float}
            # others as {key: {value: float, ...}}; handle both.
            for k, v in raw_metrics.items():
                if isinstance(v, dict):
                    final_best_metrics[k] = float(v.get("value", float("nan")))
                else:
                    try:
                        final_best_metrics[k] = float(v)
                    except (TypeError, ValueError):
                        final_best_metrics[k] = float("nan")

    # --- Pre-load code for every program that was ever "best" ---
    best_codes: Dict[str, Optional[str]] = {}
    if init_id:
        best_codes[init_id] = init_code
    for nb in new_bests:
        if nb.new_id not in best_codes:
            best_codes[nb.new_id] = read_program_code(nb.new_id, output_dir)

    # --- Build lookup: program_id -> metrics from iteration records ---
    iter_metrics: Dict[str, Dict[str, float]] = {}
    for rec in iterations:
        iter_metrics.setdefault(rec.program_id, rec.metrics)
    if init_id and init_metrics:
        iter_metrics.setdefault(init_id, init_metrics)

    # --- Summary numbers ---
    n_iterations = len(iterations)
    init_score = init_metrics.get("combined_score", float("nan"))
    final_score = (
        checkpoints[-1].best_score if checkpoints else float("nan")
    )
    total_gain = final_score - init_score if (
        init_score == init_score and final_score == final_score
    ) else float("nan")

    log_name = log_path.name
    start_ts = meta.get("start_time", "unknown")
    end_ts = meta.get("end_time", "unknown")
    model = meta.get("model", "unknown")
    seed = meta.get("seed", "unknown")

    lines: List[str] = []
    a = lines.append

    # ═══ Header ══════════════════════════════════════════════════════════════
    a("# Evolution Progress Report")
    a("")
    a(f"**Log file:** `{log_name}`  ")
    a(f"**Start:** {start_ts}  **End:** {end_ts}  ")
    a(f"**Model:** `{model}`  **Seed:** {seed}  ")
    a(f"**Iterations:** {n_iterations}  **New-best events:** {len(new_bests)}  ")
    a(
        f"**Score:** {fmt(init_score)} → {fmt(final_score)}"
        f"  (Δ = {'%+.4f' % total_gain if total_gain == total_gain else 'N/A'})"
    )
    a("")

    # ═══ Source files ═════════════════════════════════════════════════════════
    a("## Source Files")
    a("")
    a("| File | Role |")
    a("|------|------|")
    a("| `initial_program.py` | Seed policy (EVOLVE-BLOCK is mutated) |")
    a("| `evaluator.py` | Fitness function — returns `combined_score` |")
    a("| `scenarios.py` | Deterministic train/holdout scenario generator |")
    a("| `config.yaml` | OpenEvolve run configuration |")
    a("")

    # ═══ Output inventory ═════════════════════════════════════════════════════
    a("## Output Inventory")
    a("")
    a("| Path | Contents |")
    a("|------|----------|")
    a(f"| `openevolve_output/logs/{log_name}` | Full run log |")
    a("| `openevolve_output/best/best_program.py` | Final best policy |")
    a("| `openevolve_output/best/best_program_info.json` | Final best metadata |")
    for ck in checkpoints:
        a(
            f"| `openevolve_output/checkpoints/checkpoint_{ck.checkpoint}/` "
            f"| {ck.n_programs} programs, best={fmt(ck.best_score)} |"
        )
    a("")

    # ═══ Iteration timeline ═══════════════════════════════════════════════════
    a("## Iteration Timeline")
    a("")
    a(
        "| Iter | Program (short) | Parent (short) | combined_score"
        " | success_rate | avg_latency_ms | avg_retry_count"
        " | useless_retries | good_switches | fail_fast | dur_s | 🌟 |"
    )
    a(
        "|------|-----------------|----------------|---------------"
        "|-------------|----------------|----------------"
        "|----------------|--------------|-----------|-------|-----|"
    )
    for rec in iterations:
        m = rec.metrics
        star = "✅" if rec.is_new_best else ""
        a(
            f"| {rec.iteration}"
            f" | `{rec.program_id[:8]}`"
            f" | `{rec.parent_id[:8]}`"
            f" | {fmt(m.get('combined_score', float('nan')))}"
            f" | {fmt(m.get('success_rate', float('nan')))}"
            f" | {fmt(m.get('avg_latency_ms', float('nan')), 2)}"
            f" | {fmt(m.get('avg_retry_count', float('nan')))}"
            f" | {fmt(m.get('useless_retries', float('nan')))}"
            f" | {fmt(m.get('good_endpoint_switches', float('nan')))}"
            f" | {fmt(m.get('good_fail_fast_decisions', float('nan')))}"
            f" | {rec.duration_s:.1f}"
            f" | {star} |"
        )
    a("")

    # ═══ Checkpoint timeline ══════════════════════════════════════════════════
    a("## Checkpoint Timeline")
    a("")
    a("| Checkpoint | Programs | Best ID (short) | combined_score |")
    a("|-----------|----------|----------------|---------------|")
    for ck in checkpoints:
        a(
            f"| {ck.checkpoint}"
            f" | {ck.n_programs}"
            f" | `{ck.best_id[:8]}`"
            f" | {fmt(ck.best_score)} |"
        )
    a("")

    # ═══ Best-solution transitions ════════════════════════════════════════════
    a("## Best-Solution Transitions")
    a("")
    if not new_bests:
        a("No new-best events occurred. The seed policy was never improved upon.")
        a("")
    else:
        for i, nb in enumerate(new_bests, 1):
            old_code = best_codes.get(nb.old_id) or ""
            new_code = best_codes.get(nb.new_id) or ""

            diff_str = ""
            if old_code and new_code:
                diff_str = unified_diff_blocks(
                    old_code,
                    new_code,
                    f"{nb.old_id[:8]} (before)",
                    f"{nb.new_id[:8]} (after)",
                )

            old_metrics = iter_metrics.get(nb.old_id, {})
            new_metrics = iter_metrics.get(nb.new_id, {})

            a(f"### Transition {i} — iteration {nb.iteration}")
            a("")
            a(f"**`{nb.old_id[:8]}` → `{nb.new_id[:8]}`**  ")
            a(
                f"combined_score: {fmt(nb.old_score)} → {fmt(nb.new_score)}"
                f"  (Δ = {'%+.4f' % nb.delta})"
            )
            a("")

            a("#### Metrics Before / After")
            a("")
            a("| Metric | Before | After | Δ |")
            a("|--------|--------|-------|---|")
            for met in METRICS:
                ov = old_metrics.get(met, float("nan"))
                nv = new_metrics.get(met, float("nan"))
                if ov == ov and nv == nv:
                    dv = nv - ov
                    sign = "+" if dv > 0 else ""
                    d_str = f"{sign}{fmt(dv)}"
                else:
                    d_str = "N/A"
                a(f"| `{met}` | {fmt(ov)} | {fmt(nv)} | {d_str} |")
            a("")

            # Changes description from program JSON (LLM-generated)
            prog_json = find_program_json(nb.new_id, output_dir)
            if prog_json:
                prog_data = json.loads(prog_json.read_text())
                changes_desc = (prog_data.get("changes_description") or "").strip()
                if changes_desc:
                    a("#### LLM-Described Changes")
                    a("")
                    # Blockquote multi-line descriptions
                    for desc_line in changes_desc.splitlines():
                        a(f"> {desc_line}" if desc_line else ">")
                    a("")

            if diff_str:
                a("#### Unified Diff (EVOLVE-BLOCK)")
                a("")
                a("```diff")
                a(diff_str.rstrip())
                a("```")
                a("")

    # ═══ Plateau analysis ═════════════════════════════════════════════════════
    a("## Plateau Analysis")
    a("")
    if not new_bests:
        a(
            "The run produced **no improvement** over the seed policy."
            f" All {n_iterations} iterations plateaued at {fmt(init_score)}."
        )
    else:
        # Find the longest gap between new-best events
        event_iters = [0] + [nb.iteration for nb in new_bests] + [n_iterations]
        gaps: List[Tuple[int, int, int]] = [
            (event_iters[j + 1] - event_iters[j], event_iters[j], event_iters[j + 1])
            for j in range(len(event_iters) - 1)
        ]
        longest = max(gaps, key=lambda g: g[0])
        a(
            f"Longest plateau: **{longest[0]} iterations**"
            f" (iterations {longest[1] + 1}–{longest[2]})."
        )
        a("")
        a(
            f"New-best events at iterations: "
            + ", ".join(str(nb.iteration) for nb in new_bests)
            + "."
        )
        a("")

    # Dangerous retries warning
    dangerous = [
        rec
        for rec in iterations
        if rec.metrics.get("dangerous_non_idempotent_retries", 0) > 0
    ]
    if dangerous:
        a(
            f"> ⚠️ **{len(dangerous)} iteration(s)** produced candidates with"
            f" `dangerous_non_idempotent_retries > 0`."
        )
    else:
        a(
            "> ✅ No candidate across any iteration produced"
            " `dangerous_non_idempotent_retries > 0`."
        )
    a("")

    # ═══ Final summary ════════════════════════════════════════════════════════
    a("## Final Summary")
    a("")
    a("| Metric | Seed (`initial_program.py`) | Final best |")
    a("|--------|----------------------------|------------|")
    for met in METRICS:
        iv = init_metrics.get(met, float("nan"))
        # Prefer best_program_info.json metrics; fall back to last new-best iteration record
        fv = final_best_metrics.get(met, float("nan"))
        if fv != fv and new_bests:  # NaN fallback
            fv = iter_metrics.get(new_bests[-1].new_id, {}).get(met, float("nan"))
        a(f"| `{met}` | {fmt(iv)} | {fmt(fv)} |")
    a("")

    if final_best_id:
        a(f"**Final best program ID:** `{final_best_id}`")
        a("")

    # ═══ Train / Holdout evaluation ══════════════════════════════════════════
    best_program_path = output_dir / "best" / "best_program.py"
    if evaluator_path is not None and evaluator_path.exists() and best_program_path.exists():
        a("## Train vs Holdout Evaluation")
        a("")
        a(
            "Live evaluation of the **seed policy** (`initial_program.py`) and the "
            "**final best program** on the deterministic train and holdout scenario sets."
        )
        a("")

        eval_matrix: Dict[str, Dict[str, Dict[str, float]]] = {}
        labels = {
            "seed": initial_program_path,
            "best": best_program_path,
        }
        for label, prog_path in labels.items():
            eval_matrix[label] = {}
            for dataset in ("train", "holdout"):
                print(f"  Evaluating {label}/{dataset} …", file=sys.stderr)
                eval_matrix[label][dataset] = run_evaluator(
                    prog_path, dataset, evaluator_path, python_exe
                )

        for dataset in ("train", "holdout"):
            a(f"### {dataset.capitalize()} Dataset")
            a("")
            seed_res = eval_matrix.get("seed", {}).get(dataset, {})
            best_res = eval_matrix.get("best", {}).get(dataset, {})

            a("| Metric | Seed | Best | Δ (best − seed) |")
            a("|--------|------|------|-----------------|")
            for met in METRICS:
                sv = seed_res.get(met, float("nan"))
                bv = best_res.get(met, float("nan"))
                if sv == sv and bv == bv:
                    dv = bv - sv
                    sign = "+" if dv > 0 else ""
                    d_str = f"{sign}{fmt(dv)}"
                else:
                    d_str = "N/A"
                a(f"| `{met}` | {fmt(sv)} | {fmt(bv)} | {d_str} |")
            a("")

    a("---")
    a(f"*Report generated by `scripts/generate_report.py` from `{log_name}`.*")

    return "\n".join(lines)


# ── CLI ────────────────────────────────────────────────────────────────────────


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate a detailed evolution-progress markdown report from an OpenEvolve log."
    )
    parser.add_argument(
        "--log",
        type=Path,
        default=None,
        help="Path to the log file. Defaults to the latest *.log in <output-dir>/logs/.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help=(
            "Output markdown file path. "
            "Defaults to docs/evolution_progress_<log-stem>.md."
        ),
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("openevolve_output"),
        help="OpenEvolve output directory (default: openevolve_output).",
    )
    parser.add_argument(
        "--initial-program",
        type=Path,
        default=Path("initial_program.py"),
        help="Path to initial_program.py (default: initial_program.py).",
    )
    parser.add_argument(
        "--evaluator",
        type=Path,
        default=Path("evaluator.py"),
        help="Path to evaluator.py for live train/holdout comparison (default: evaluator.py).",
    )
    parser.add_argument(
        "--python",
        default=sys.executable,
        help="Python executable to use when running the evaluator (default: current interpreter).",
    )
    parser.add_argument(
        "--no-eval",
        action="store_true",
        help="Skip live train/holdout evaluation (faster, report uses only log data).",
    )
    args = parser.parse_args()

    output_dir = args.output_dir.resolve()
    initial_program = args.initial_program.resolve()

    # Resolve log file
    if args.log:
        log_path = args.log.resolve()
    else:
        log_dir = output_dir / "logs"
        available = sorted(log_dir.glob("*.log"))
        if not available:
            print(f"ERROR: No *.log files found in {log_dir}", file=sys.stderr)
            sys.exit(1)
        log_path = available[-1]
        print(f"Auto-selected latest log: {log_path}")

    if not log_path.exists():
        print(f"ERROR: Log file not found: {log_path}", file=sys.stderr)
        sys.exit(1)

    if not initial_program.exists():
        print(f"ERROR: Initial program not found: {initial_program}", file=sys.stderr)
        sys.exit(1)

    # Resolve output path
    if args.output:
        out_path = args.output.resolve()
    else:
        out_path = (Path("docs") / f"evolution_progress_{log_path.stem}.md").resolve()

    evaluator_path: Path | None = None
    if not args.no_eval:
        evaluator_path = args.evaluator.resolve()
        if not evaluator_path.exists():
            print(
                f"WARNING: evaluator not found at {evaluator_path}; skipping live eval.",
                file=sys.stderr,
            )
            evaluator_path = None

    report = generate_report(
        log_path, output_dir, initial_program,
        evaluator_path=evaluator_path,
        python_exe=args.python,
    )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(report)
    print(f"Report written to: {out_path}")
    print(f"  Lines: {len(report.splitlines())}")
    print(f"  New-best events captured in report.")


if __name__ == "__main__":
    main()
