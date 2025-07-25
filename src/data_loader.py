import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(path):
    df = pd.read_csv(path)

    # التأكد من وجود الأعمدة اللازمة
    required_columns = [
        "pickup_longitude", "pickup_latitude",
        "dropoff_longitude", "dropoff_latitude",
        "passenger_count", "pickup_datetime", "fare_amount"
    ]
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"العمود '{col}' غير موجود في البيانات!")

    # تحويل التاريخ واستخراج الميزات الزمانية
    df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"])
    df["hour"] = df["pickup_datetime"].dt.hour
    df["day"] = df["pickup_datetime"].dt.dayofweek

    # حذف القيم الناقصة والبيانات الغريبة
    df = df.dropna()
    df = df[(df["fare_amount"] > 0) & (df["passenger_count"] > 0)]

    # اختيار الميزات والهدف
    features = [
        "pickup_longitude", "pickup_latitude",
        "dropoff_longitude", "dropoff_latitude",
        "passenger_count", "hour", "day"
    ]
    X = df[features]
    y = df["fare_amount"]

    # تقسيم البيانات
    return train_test_split(X, y, test_size=0.2, random_state=42)
