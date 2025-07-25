
# NYC Taxi Fare Prediction - MLOps Project 🗽🚕

Проект по предсказанию стоимости поездки на такси в Нью-Йорке с использованием подхода MLOps.

## 📦 Стек технологий:
- Python 3.10
- Scikit-learn
- FastAPI
- Uvicorn
- Pytest
- Docker
- GitHub Actions

## 🎯 Цель
Создать end-to-end MLOps pipeline:
- Предобработка данных
- Обучение модели
- Автоматическое тестирование
- Инференс (предсказание)
- Docker контейнеризация
- CI/CD через GitHub Actions
- REST API с FastAPI

## 📁 Структура проекта
```
.
├── data/                  # CSV файл с данными
├── src/
│   ├── data_loader.py     # Загрузка и обработка данных
│   ├── train.py           # Обучение модели
│   ├── inference.py       # Предсказания
│   └── app.py             # FastAPI API
├── tests/                 # Тесты на Pytest
├── models/                # Сохранённая модель
├── Dockerfile             # Docker-контейнер
├── requirements.txt       # Python-зависимости
└── .github/workflows/ci.yml  # GitHub Actions pipeline
```

## 🚀 Запуск локально
### Установка зависимостей
```bash
pip install -r requirements.txt
```

### Обучение модели
```bash
python src/train.py
```

### Предсказания
```bash
python src/inference.py
```

### Запуск API
```bash
uvicorn src.app:app --reload
```

## 🐳 Docker
### Сборка и запуск
```bash
docker build -t nyc-taxi-api .
docker run -p 8000:8000 nyc-taxi-api
```

## 🔁 CI/CD
GitHub Actions автоматически запускает:
- Тесты
- Обучение модели
- Инференс

## 📫 Endpoint API
- `GET /` — Стартовая страница
- `POST /predict` — Предсказание стоимости поездки

Пример запроса:
```json
{
  "pickup_longitude": -73.978165,
  "pickup_latitude": 40.757977,
  "dropoff_longitude": -73.989838,
  "dropoff_latitude": 40.751171,
  "passenger_count": 1,
  "hour": 16,
  "day": 1
}
```

---

🛠 Разработано в рамках учебного MLOps проекта.
