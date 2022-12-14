FROM python:3.9-alpine

COPY . /app
WORKDIR /app

RUN pip3 install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python", "-u", "main.py"]

