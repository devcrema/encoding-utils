import sys
import base64
from hashlib import sha256
import urllib
import pyperclip


def utf8_decode(str): # utf8 str -> bytes
    return str.encode('utf-8')

def utf8_encode(bytes): # bytes -> utf8 str
    return bytes.decode('utf-8', 'ignore')

def euc_kr_decode(str): # euc-kr str -> bytes
    return str.encode('euc-kr')

def euc_kr_encode(bytes): # bytes -> euc-kr str
    return bytes.decode('euc-kr', 'ignore')

def base64_decode(str): # base64 str -> plain bytes
    return base64.b64decode(str + "==")

def base64_encode(bytes): # plain bytes -> base64 str
    return base64.b64encode(bytes).decode('ascii')

def base64_url_decode(str): # base64 str -> plain bytes
    return base64.urlsafe_b64decode(str + "==") # python에서 알아서 == 제거해줌

def base64_url_encode(bytes): # plain bytes -> base64 str
    return base64.urlsafe_b64encode(bytes).decode('ascii')

def hex_decode(str): # hex str -> bytes
    return bytes.fromhex(str)

def hex_encode(bytes): # bytes -> hex str
    return bytes.hex()

def sha256_decode(str): # sha 256 hex str -> bytes
    raise bytes.fromhex(str)

def sha256_encode(bytes): # bytes -> sha256 hex
    return sha256(bytes).hexdigest()

def url_decode(str): # url str -> bytes
    return urllib.parse.unquote(str).encode('utf-8')

def url_encode(bytes): # bytes -> url encode str
    return urllib.parse.quote(bytes.decode('utf-8', 'ignore'))

encode_func = {
    'text': (utf8_decode, utf8_encode),
    'utf8': (utf8_decode, utf8_encode),
    'euckr': (euc_kr_decode, euc_kr_encode),
    'base64': (base64_decode, base64_encode),
    'base64url': (base64_url_decode, base64_url_encode),
    'hex': (hex_decode, hex_encode),
    'sha256': (sha256_decode, sha256_encode),
    'url': (url_decode, url_encode)
}

# 모든 bytes의 기준은 unicode
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
    print(result)
    print(f'변환 완료! [{current}][{len(bytes)} bytes] -> [{next}][{len(result)} length]')
    print("클립보드에 복사됨!")
