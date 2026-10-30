FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DB_PATH=/app/data/midias.db

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY crud_filmes_e_series.py db.py index.html seed_midias.py ./

RUN mkdir -p /app/data

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "crud_filmes_e_series:app", "--host", "0.0.0.0", "--port", "8000"]