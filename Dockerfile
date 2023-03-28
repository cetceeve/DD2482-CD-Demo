FROM python:3.11.2-slim-bullseye

WORKDIR /app

RUN pip3 install Flask flask-cors

COPY . .

CMD [ "python", "./src/staticServer.py" ]