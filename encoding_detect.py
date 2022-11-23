#!/usr/bin/env python3

# Raycast Script Command Template
#
# Duplicate this file and remove ".template." from the filename to get started.
# See full documentation here: https://github.com/raycast/script-commands
#
# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title encoding-detect
# @raycast.mode fullOutput
#
# Optional parameters:
# @raycast.icon 📝
# @raycast.packageName encoding-detect


import base64
import subprocess
import sys
import pkg_resources

required = {'pyperclip', 'chardet'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed
if missing:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

import pyperclip
import chardet


def make_result_text(is_match, confidence, byte_length):
    return "match: " + is_match.__str__() + ", confidence: " + confidence.__str__() + "%, byteSize: " + byte_length.__str__()


def utf8_detect(str):
    bytes = str.encode('utf-8')
    result = chardet.detect(bytes)
    match = result['encoding'].lower() == 'utf-8'
    return make_result_text(match, result['confidence'] * 100, len(bytes))


def euc_kr_detect(str):
    bytes = str.encode('euc-kr')
    result = chardet.detect(bytes)
    match = result['encoding'].lower() == 'euc-kr'
    return make_result_text(match, result['confidence'] * 100, len(bytes))


def base64_detect(str):
    try:
        bytes = base64.b64decode(str + "==")
        return make_result_text(True, 100, len(bytes))
    except:
        return make_result_text(False, 0, 0)

def hex_detect(str):
    try:
        bytes = bytes.fromhex(str)
        return make_result_text(True, 100, len(bytes))
    except:
        return make_result_text(False, 0, 0)

# base64 or hex encoded sha256
def sha256_detect(str):
    try:
        bytes = bytes.fromhex(str)
        confidence = 0
        if len(bytes) == 32:
            confidence = 100
        print("hex sha256")
        return make_result_text(True, confidence, len(bytes))
    except:
        try:
            bytes = base64.b64decode(str + "==")
            confidence = 0
            if len(bytes) == 32:
                confidence = 100
            print("base64 sha256")
            return make_result_text(True, confidence, len(bytes))
        except:
            return make_result_text(False, 0, 0)


detect_func = {
    'utf-8': utf8_detect,
    'euc-kr': euc_kr_detect,
    'base64': base64_detect,
    'hex': hex_detect,
    'sha-256': sha256_detect,
    # pkcs7
    # pkcs1
    # pkcs10
    # x509
}

# 모든 bytes의 기준은 unicode
if __name__ == '__main__':
    target = pyperclip.paste() # 클립보드에서 텍스트 가져오기
    print("[" + target + "]")
    length = len(target)
    print("length: " + length.__str__() + ", " + (length / 1024).__str__() + "k")
    for k, v in detect_func.items():
        result = v(target)
        print(k + " : " + result)

