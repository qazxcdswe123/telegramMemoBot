FROM python:3.11.3-alpine3.17

COPY . /app
WORKDIR /app

RUN pip3 install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python", "-u", "main.py"]