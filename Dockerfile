FROM python:3.5

ENV PYTHONUNBUFFERED 1

#COPY . /api

COPY migrations /api/migrations
COPY requirements.txt /api/requirements.txt
COPY app.py /api/app.py

WORKDIR /api


RUN pip install -r /api/requirements.txt
RUN flask db upgrade

EXPOSE 80

CMD gunicorn -b 0.0.0.0:80 app:app
