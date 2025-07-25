
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Инициализация FastAPI приложения
app = FastAPI()

# Загрузка модели
model = joblib.load("models/model.joblib")

# Класс данных для запроса
class TaxiTrip(BaseModel):
    pickup_longitude: float
    pickup_latitude: float
    dropoff_longitude: float
    dropoff_latitude: float
    passenger_count: int
    hour: int
    day: int

# Корневой маршрут
@app.get("/")
def read_root():
    return {"message": "Прогноз тарифа NYC Taxi"}

# Маршрут для предсказания тарифа
@app.post("/predict")
def predict_fare(trip: TaxiTrip):
    # Подготовка данных к модели
    features = np.array([[trip.pickup_longitude, trip.pickup_latitude,
                          trip.dropoff_longitude, trip.dropoff_latitude,
                          trip.passenger_count, trip.hour, trip.day]])

    # Предсказание
    prediction = model.predict(features)[0]
    return {"predicted_fare": round(prediction, 2)}
