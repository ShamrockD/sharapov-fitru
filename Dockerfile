# Используем официальный Python образ
FROM python:3.13-slim-bullseye

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Создаем и переходим в рабочую директорию
WORKDIR /app/sharapov_fit

# Копируем файл с зависимостями и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY sharapov_fit/ .

# Создаем нужную директорию
RUN mkdir -p /app/sharapov_fit/staticfiles/

# Собираем статику (если используете)
RUN python manage.py collectstatic --noinput

# Открываем порт
EXPOSE 8000

# Запускаем сервер
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "sharapov_fit.wsgi:application"]