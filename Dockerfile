FROM python:3.10.9-slim-buster

WORKDIR /app

ADD . /app

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "-b", ":5000", "app:app"]
