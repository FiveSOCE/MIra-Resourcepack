#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

IMPORT_DIR=".import/pyro"
MODEL_DIR="assets/weapons_vol_17/models/weapons_vol_17"
TEXTURE_DIR="assets/weapons_vol_17/textures/weapons_vol_17"

mkdir -p "$MODEL_DIR" "$TEXTURE_DIR"

cat "$IMPORT_DIR"/thalorien_war_axe.json.b64.* | base64 --decode > "$MODEL_DIR/thalorien_war_axe.json"
cat "$IMPORT_DIR"/thalorien_war_axe.png.b64.* | base64 --decode > "$TEXTURE_DIR/thalorien_war_axe.png"
cat "$IMPORT_DIR"/thalorien_war_axe.png.mcmeta.b64.* | base64 --decode > "$TEXTURE_DIR/thalorien_war_axe.png.mcmeta"
cat "$IMPORT_DIR"/thalorien_war_axe_vfx.png.b64.* | base64 --decode > "$TEXTURE_DIR/thalorien_war_axe_vfx.png"
cat "$IMPORT_DIR"/thalorien_war_axe_vfx.png.mcmeta.b64.* | base64 --decode > "$TEXTURE_DIR/thalorien_war_axe_vfx.png.mcmeta"

# Sanity-check the generated files before they are packed.
test -s "$MODEL_DIR/thalorien_war_axe.json"
test -s "$TEXTURE_DIR/thalorien_war_axe.png"
test -s "$TEXTURE_DIR/thalorien_war_axe_vfx.png"

python3 - <<'PY'
import json
from pathlib import Path
json.loads(Path('assets/weapons_vol_17/models/weapons_vol_17/thalorien_war_axe.json').read_text())
json.loads(Path('assets/weapons_vol_17/textures/weapons_vol_17/thalorien_war_axe.png.mcmeta').read_text())
json.loads(Path('assets/weapons_vol_17/textures/weapons_vol_17/thalorien_war_axe_vfx.png.mcmeta').read_text())
PY
