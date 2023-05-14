FROM python:3.10.9-slim-buster

WORKDIR /app

ADD . /app

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "-t", "120", "-b", ":5000", "app:app"]
