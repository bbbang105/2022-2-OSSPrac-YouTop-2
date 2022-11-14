# 사용할 이미지 설정
FROM tiangolo/uwsgi-nginx-flask:python3.8 
# python 컨테이너에서 사용되는 경로
WORKDIR /usr/src/app
# 현재 local 경로에 있는 폴더(2022_2_OSSPrac_YouTop_2_main)를 컨테이너 내부로 copy함
COPY . .
#  TeamHw_5_Code로 이동한 후, main.py을 실행함
CMD ["python", "./TeamHw_5_Code/main.py"]
