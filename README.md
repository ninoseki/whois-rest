# whois-rest

A RESTful `whois`.

## Installation

```bash
$ pip install poetry
$ poetry install

$ uvicorn app:app
INFO:     Started server process [64616]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

## Usage

```bash
curl localhost:8000/api/v1/{domain}

curl localhost:8000/api/v1/google.com
```
