FROM python:3.8-slim
WORKDIR /app
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*
COPY ../src/python/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/python/ .
CMD ["python", "extract_transform.py"]