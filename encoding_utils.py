#!/usr/bin/env python3

# Raycast Script Command Template
#
# Duplicate this file and remove ".template." from the filename to get started.
# See full documentation here: https://github.com/raycast/script-commands
#
# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title encoding-utils
# @raycast.mode fullOutput
#
# Optional parameters:
# @raycast.icon 📝
# @raycast.packageName encoding-utils
# @raycast.argument1 { "type": "text", "placeholder": "current encoding", "percentEncoded": false, "secure": false, "optional": true }
# @raycast.argument2 { "type": "text", "placeholder": "next encoding", "percentEncoded": false, "secure": false, "optional": true }
import sys
import pyperclip
import base64

def utf8_decode(str): # utf8 str -> bytes
    return str.encode('utf-8')

def utf8_encode(bytes): # bytes -> utf8 str
    return bytes.decode('utf-8')

def base64_decode(str): # base64 str -> plain bytes
    return base64.b64decode(str)

def base64_encode(bytes): # plain bytes -> base64 str
    return base64.b64encode(bytes).decode('ascii')

encode_func = {
    'utf8': (utf8_decode, utf8_encode),
    'base64': (base64_decode, base64_encode),
    'hex': (hex_decode, hex_encode),
}

if __name__ == '__main__':
    current = sys.argv[1].lower().replace("-", "") # 기존
    if not current:
        current = 'utf8' # 기본값
    next = sys.argv[2].lower().replace("-", "") # 인코딩
    if not next:
        next = 'utf8' # 기본값
    target = pyperclip.paste() # 클립보드에서 텍스트 가져오기
    bytes = encode_func[current][0](target) # 변환 함수 dict에서 bytes로 변환
    result = encode_func[next][1](bytes) # 변환 함수 dict에서 bytes에서 대상인코딩으로 변환
    # 클립보드에 다시 넣기
    pyperclip.copy(result)
    print("변환 완료!" + current + " -> " + next + " : " + result)