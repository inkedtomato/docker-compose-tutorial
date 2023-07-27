# 베이스 이미지 설정
FROM python:3.9

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 파일 복사
COPY ./requirements.txt /app/requirements.txt
COPY ./app.py /app/app.py

# 필요한 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# FLASK 앱 실행
CMD ["python", "app.py"]
