# Placement Arena — Dockerfile for Production Deployment
FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY backend/requirements.txt /app/backend/
RUN pip install --no-cache-dir -r backend/requirements.txt

# Copy project files
COPY backend /app/backend
COPY frontend /app/frontend

WORKDIR /app/backend

# Collect static files & run migrations during startup
EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py create_initial_data && python manage.py seed_questions && python manage.py create_daily_exam && gunicorn placement_arena.wsgi:application --bind 0.0.0.0:8000"]
