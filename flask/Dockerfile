FROM python:3.8.10-slim

WORKDIR /app

ADD . .

RUN pip install -r requirements.txt

CMD ["gunicorn","-w", "5", "-b", "0.0.0.0:8080", "app:app"]