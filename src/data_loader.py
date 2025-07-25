
import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """
    Загружает и предварительно обрабатывает данные поездок Uber.
    :param path: Путь к CSV файлу с данными
    :return: Обработанный DataFrame
    """
    # Загрузка CSV
    df = pd.read_csv(path)

    # Преобразование даты и времени в datetime
    df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"])

    # Извлечение признаков времени
    df["hour"] = df["pickup_datetime"].dt.hour
    df["day"] = df["pickup_datetime"].dt.dayofweek

    return df
