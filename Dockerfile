FROM tiangolo/uwsgi-nginx-flask:python3.8
# 위 이미지를 베이스 이미지로 사용한다.

COPY . /app
# 현재 디렉토리의 파일들을 카피한다.
