FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY pyproject.toml pyproject.toml
RUN poetry install --no-interaction --no-ansi

RUN apt-get clean