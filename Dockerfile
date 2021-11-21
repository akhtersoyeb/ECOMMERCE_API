# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

ENV PYTHONUNBUFFERED=1

RUN pip3 install pipenv

COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy --ignore-pipfile

COPY . .

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
