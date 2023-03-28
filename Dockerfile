FROM python:3.11.2-slim-bullseye

WORKDIR /app

RUN pip3 install Flask flask-cors

COPY . .

EXPOSE 5000
RUN chmod +x ./entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]