import joblib
from src.data_loader import load_data

# Загрузка модели
model = joblib.load("models/model.joblib")

# Загрузка новых данных
inference_data_path = "data/uber.csv"
df = load_data(inference_data_path)

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

print(
    "Предсказания завершены. "
    "Результаты сохранены в 'inference_results.csv'"
)
