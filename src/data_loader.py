import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(path):
    # تحميل البيانات
    df = pd.read_csv(path)

    # حذف القيم الناقصة (لو فيه)
    df = df.dropna()

    # تحديد الميزات (X) والهدف (y)
    X = df[[
        "pickup_longitude", "pickup_latitude",
        "dropoff_longitude", "dropoff_latitude",
        "passenger_count"
    ]]
    y = df["fare_amount"] if "fare_amount" in df.columns else df.iloc[:, -1]  # عمود الهدف لو موجود

    # تقسيم البيانات
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    return X_train, X_test, y_train, y_test
