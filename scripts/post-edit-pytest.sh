#!/usr/bin/env bash
# PostToolUse hook: run pytest after Python file edits.
# Exits 0 with a systemMessage on failure (warn, don't block).

set -euo pipefail

# Read hook input from stdin
INPUT=$(cat)

# Only act on file-edit tools that touched a .py file
TOOL=$(echo "$INPUT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('toolName',''))" 2>/dev/null || true)
FILE=$(echo "$INPUT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('toolInput',{}).get('filePath',''))" 2>/dev/null || true)

case "$TOOL" in
  create_file|replace_string_in_file|multi_replace_string_in_file) ;;
  *) exit 0 ;;
esac

if [[ "$FILE" != *.py ]]; then
  exit 0
fi

# Run pytest quietly; capture output
if OUTPUT=$(python3 -m pytest -q 2>&1); then
  exit 0
fi

# Tests failed — emit warning via systemMessage
cat <<EOF
{
  "decision": "continue",
  "systemMessage": "pytest failed after editing $FILE:\n$OUTPUT"
}
EOF
