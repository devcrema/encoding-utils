#!/bin/bash

# Raycast Script Command Template
#
# Duplicate this file and remove ".template." from the filename to get started.
# See full documentation here: https://github.com/raycast/script-commands
#
# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title rand-utils
# @raycast.mode fullOutput
#
# Optional parameters:
# @raycast.icon 📝
# @raycast.packageName encoding-utils
# @raycast.argument1 { "type": "text", "placeholder": "rand, randstr, secret", "percentEncoded": false, "secure": false, "optional": true }
# @raycast.argument2 { "type": "text", "placeholder": "size", "percentEncoded": false, "secure": false, "optional": true }

PYTHON_SCRIPT=rand_utils.py

./common_script.sh "$PYTHON_SCRIPT" "$@"
