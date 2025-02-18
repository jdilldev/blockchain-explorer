# Start venv

. .venv/bin/activate

# Run Flask app locally

flask run

# Build docker image

docker build --tag python-docker .

# Run flask container

docker run -d -p 5000:5000 blockchain-explorer

# Run react container

docker run -p 80:80 ui

# Sample eth address

0xc94770007dda54cF92009BFF0dE90c06F603a09f

# Hosted on AWS

http://18.233.163.124:5000/address/balance/0xc94770007dda54cF92009BFF0dE90c06F603a09f

```
# UI Dockerfile
# react app

# pull official base image
FROM node:20-alpine

# set working directory
WORKDIR /ui

# install and cache app dependencies
COPY package.json .
COPY package-lock.json .
RUN npm ci

# start app
CMD ["npm", "run", "dev"]
```
