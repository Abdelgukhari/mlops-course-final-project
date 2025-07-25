
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib
import os

# Загрузка и обработка данных
DATA_PATH = "data/uber.csv"
df = pd.read_csv(DATA_PATH)
df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"])
df["hour"] = df["pickup_datetime"].dt.hour
df["day"] = df["pickup_datetime"].dt.dayofweek

# Удаление пропусков и выбросов
df = df.dropna()
df = df[(df["fare_amount"] > 0) & (df["passenger_count"] > 0)]

# Выбор признаков и целевой переменной
features = ["pickup_longitude", "pickup_latitude", "dropoff_longitude", 
            "dropoff_latitude", "passenger_count", "hour", "day"]
target = "fare_amount"

X = df[features]
y = df[target]

# Разделение на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучение модели линейной регрессии
model = LinearRegression()
model.fit(X_train, y_train)

# Оценка качества модели
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f"Среднеквадратичная ошибка (MSE): {mse:.2f}")

# Сохранение модели
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/model.joblib")
