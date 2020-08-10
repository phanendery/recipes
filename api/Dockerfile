FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app/api

COPY . .

RUN pip install --no-cache-dir -r ./requirements.txt

ARG flask_app
ARG flask_env
ARG database_uri

ENV FLASK_APP $flask_app
ENV FLASK_ENV $flask_env
ENV DATABASE_URI $database_uri

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "sh" ]

CMD [ "docker_entrypoint.sh" ]