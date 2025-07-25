
# Используем официальный легковесный образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем все файлы проекта внутрь контейнера
COPY . .

# Устанавливаем зависимости
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Открываем порт для сервера
EXPOSE 8000

# Команда для запуска FastAPI-приложения
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
