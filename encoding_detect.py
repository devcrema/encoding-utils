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


import sys
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

# TODO str hex, base64 decode해보고 에러나는지 확인
# TODO str을 hex, base64 decode해서 sha256, md5 등등 각각 길이 맞는지 점검하기

detect_func = {
    'utf-8': utf8_detect,
    'euc-kr': euc_kr_detect,
    # 'base64': utf8_detect,
    # 'hex': utf8_detect,
    # 'sha-256': utf8_detect,
}

# 모든 bytes의 기준은 unicode
if __name__ == '__main__':
    target = pyperclip.paste() # 클립보드에서 텍스트 가져오기
    print("[" + target + "]")
    for k, v in detect_func.items():
        result = v(target)
        print(k + " : " + result)

