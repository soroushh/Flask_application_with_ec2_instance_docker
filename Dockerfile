FROM ubuntu:18.04

MAINTAINER sorush.kh68@gmail.com

RUN apt-get update -y
RUN apt-get install python3-pip -y
RUN apt-get install gunicorn3 -y

COPY requirements.txt requirements.txt
COPY flask_app /opt/

RUN pip3 install -r requirements.txt

WORKDIR /opt/

CMD ["gunicorn3", "-b", "0.0.0.0:8000", "flask_app:app", "--workers=5"]
