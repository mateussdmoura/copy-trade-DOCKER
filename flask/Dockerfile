FROM python:3.8.10-slim

WORKDIR /app

ADD . /app

RUN pip3 install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:8080 app:app