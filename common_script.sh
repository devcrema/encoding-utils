#!/bin/bash

# 가상환경 체크 및 생성
VENV_DIR=".venv"
if [ ! -d "$VENV_DIR" ]; then
  echo "Creating virtual environment..."
  python3 -m venv $VENV_DIR
fi

# 가상환경 활성화
source $VENV_DIR/bin/activate

# 필요한 패키지 설치
pip install -r requirements.txt --quiet

# 인자 체크
if [ "$#" -lt 1 ]; then
  echo "Usage: ./common_script.sh ~~.py <arg1> [arg2] [arg3] ..."
  deactivate
  exit 1
fi

# Python 스크립트와 인자 추출
SCRIPT_FILE="$1"
shift  # 첫 번째 인자를 제거

# Python 스크립트 실행
python3 "$SCRIPT_FILE" "$@"

# 가상환경 비활성화
deactivate