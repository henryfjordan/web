FROM python:3

RUN pip install requests flask

ENV FLASK_APP=/server/webhook.py
ENV PYTHONUNBUFFERED=0

EXPOSE 5000

ADD ./server /server

CMD [ "flask", "run", "-h", "0.0.0.0"]
