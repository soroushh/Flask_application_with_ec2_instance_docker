FROM ubuntu:18.04

MAINTAINER sorush.kh68@gmail.com

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -y
RUN apt-get install python3-pip -y
RUN apt-get install gunicorn3 -y
RUN apt-get install python-psycopg2 -y
RUN apt-get install -y python-alembic

COPY requirements.txt requirements.txt
RUN mkdir /app
COPY . /app/

RUN pip3 install -r requirements.txt

WORKDIR /app

CMD ["gunicorn3", "-b", "0.0.0.0:8000", "flask_app.routes:app", "--workers=5"]
