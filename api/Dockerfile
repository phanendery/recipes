FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app/api

COPY . .

RUN pip install -r ./requirements.txt

EXPOSE 5000

RUN ./docker_entrypoint.sh