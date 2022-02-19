# prod env
FROM python:3.9-slim-buster

RUN apt-get update \
  && apt-get install -y \
  whois \
  && apt-get clean  \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /whois-rest

COPY pyproject.toml poetry.lock gunicorn.conf.py /whois-rest/
COPY app /whois-rest/app

RUN pip3 install poetry \
  && poetry config virtualenvs.create false \
  && poetry install --no-dev

ENV PORT 8000

EXPOSE $PORT

CMD gunicorn -k uvicorn.workers.UvicornWorker app:app
