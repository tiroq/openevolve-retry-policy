import json
import sys
import os

def extract_evolve_block(code):
    lines = code.splitlines()
    start = -1
    end = -1
    for i, line in enumerate(lines):
        if "# EVOLVE-BLOCK-START" in line:
            start = i
        if "# EVOLVE-BLOCK-END" in line:
            end = i
            break
    if start != -1 and end != -1:
        return "\n".join(lines[start:end+1])
    return code

ids = ["61b091ad", "57e93334", "b49caea0", "39cfe3ca", "8e3390ac", "f77abb78"]
files = {
    "61b091ad": "initial_program.py",
    "57e93334": "openevolve_output/checkpoints/checkpoint_50/programs/57e93334-be2b-455c-b98e-8bc43b90c6b7.json",
    "b49caea0": "openevolve_output/checkpoints/checkpoint_50/programs/b49caea0-f858-4a2c-9873-75d973cac79a.json",
    "39cfe3ca": "openevolve_output/checkpoints/checkpoint_50/programs/39cfe3ca-9629-4338-823a-f0da63eeb97f.json",
    "8e3390ac": "openevolve_output/checkpoints/checkpoint_50/programs/8e3390ac-14e3-4c36-9dda-1f18ffdd6b45.json",
    "f77abb78": "openevolve_output/checkpoints/checkpoint_50/programs/f77abb78-428e-46ac-9319-1fad1a862add.json"
}

os.makedirs("temp_blocks", exist_ok=True)

for id_short, path in files.items():
    if path.endswith(".json"):
        with open(path, 'r') as f:
            data = json.load(f)
            code = data['code']
    else:
        with open(path, 'r') as f:
            code = f.read()
    
    block = extract_evolve_block(code)
    with open(f"temp_blocks/{id_short}.py", 'w') as f:
        f.write(block + "\n")
