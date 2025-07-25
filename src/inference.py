import pandas as pd
import joblib

# Загрузка модели
model = joblib.load("models/model.joblib")

# Загрузка новых данных
inference_data_path = "data/uber.csv"
df = pd.read_csv(inference_data_path)

# Предобработка даты и времени
df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"])
df["hour"] = df["pickup_datetime"].dt.hour
df["day"] = df["pickup_datetime"].dt.dayofweek

# Удаление пропущенных значений
df = df.dropna()

# Выбор признаков
features = [
    "pickup_longitude", "pickup_latitude", "dropoff_longitude",
    "dropoff_latitude", "passenger_count", "hour", "day"
]
X = df[features]

# Прогнозирование
predictions = model.predict(X)

# Добавление предсказаний в DataFrame
df["predicted_fare"] = predictions

# Сохранение результатов
df[["pickup_datetime", "predicted_fare"]].to_csv(
    "inference_results.csv", index=False
)

print("✅ تم الانتهاء من التنبؤ. النتائج محفوظة في 'inference_results.csv'")
