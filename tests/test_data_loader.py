
import pytest
from src.data_loader import load_data

def test_load_data_shape():
    """
    Проверяет, что после загрузки данные не пустые и содержат нужные столбцы.
    """
    df = load_data("data/nyc-taxi-sample.csv")

    # Проверка, что данные не пустые
    assert not df.empty, "Данные пустые!"

    # Проверка наличия основных колонок
    expected_columns = ["pickup_datetime", "pickup_longitude", "pickup_latitude",
                        "dropoff_longitude", "dropoff_latitude", "passenger_count",
                        "hour", "day"]
    for col in expected_columns:
        assert col in df.columns, f"Колонка '{col}' отсутствует!"
