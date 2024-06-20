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
    node-npm \
    make \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY pyproject.toml pyproject.toml
RUN poetry install --no-interaction --no-ansi

COPY package.json package-lock.json /app/
RUN npm install

COPY . .
RUN npm run build
RUN npm install -D tailwindcss@latest postcss@latest autoprefixer@latest
RUN npx tailwindcss init
RUN npm install bootstrap
RUN npm install @popperjs/core