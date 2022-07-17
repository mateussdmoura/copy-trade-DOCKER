FROM python:3.8.10

WORKDIR /app

ADD . /app

RUN pip3 install -r requirements.txt

CMD [ "uswgi", "app.ini" ]