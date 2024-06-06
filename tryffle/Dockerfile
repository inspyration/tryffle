FROM node:16 AS node-builder

# Définir le répertoire de travail pour Node.js
WORKDIR /app

# Copier les fichiers package.json et package-lock.json
COPY package*.json ./

# Installer les dépendances Node.js
RUN npm install

RUN npm install vite

# Copier le reste des fichiers de l'application
COPY . .

# Exécuter le build Vite
RUN npm run build

FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-fra \
    libtesseract-dev \
    poppler-data \
    poppler-utils \
    libpoppler-dev \
    libpoppler-cpp-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY pyproject.toml pyproject.toml
RUN poetry install --no-interaction --no-ansi
