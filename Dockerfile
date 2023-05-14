FROM python:3.10.9-slim-buster

WORKDIR /app

ADD . /app

RUN pip3 install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python3", "app.py"]
