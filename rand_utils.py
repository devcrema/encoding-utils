#!/usr/bin/env python3

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
import string
import subprocess
import sys
import pkg_resources
import secrets
import base64

required = {'pyperclip'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed
if missing:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

import pyperclip


def rand_number(size):
    result=''
    for i in range(0,size):
        result += secrets.randbelow(10).__str__()
    return result

def rand_string(size):
    result=''
    elements = string.digits + string.ascii_lowercase
    for i in range(0,size):
        result += secrets.choice(elements)
    return result

def secret_token(size):
    secret_bytes = secrets.token_bytes(size)
    return base64.b64encode(secret_bytes).decode(‘ascii’)


encode_func = {
    'rand': (rand_number),
    'randstr': (rand_string),
    'secret': (secret_token)
}

# 모든 bytes의 기준은 unicode
if __name__ == '__main__':
    method = sys.argv[1].lower().replace("-", "") # 기존
    if not method:
        method = 'rand' # 기본값
    size = sys.argv[2].lower().replace("-", "") # 인코딩
    if not size:
        size = '10' # 기본값
    result = encode_func[method](int(size))
    # 클립보드에 다시 넣기
    pyperclip.copy(result)
    print(result)
    print(f'rand 완료! [{method}][{size}] -> [{len(result)} length]')
    print("클립보드에 복사됨!")
