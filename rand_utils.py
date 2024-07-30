import string
import sys
import secrets
import base64
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
    return base64.b64encode(secret_bytes).decode('ascii')


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
