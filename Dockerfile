# syntax=docker/dockerfile:1

FROM python:3.11.11-slim-bullseye

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

WORKDIR /app
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]