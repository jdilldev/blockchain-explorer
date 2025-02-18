# syntax=docker/dockerfile:1

# flask app
FROM python:3.11.11-slim-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"] 
# TODO move to production https://flask.palletsprojects.com/en/stable/tutorial/deploy/

