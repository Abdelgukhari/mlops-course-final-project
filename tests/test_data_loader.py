from src.data_loader import load_data


def test_load_data_shape():
    """
    Проверяет, что после загрузки данные не пустые и содержат нужные столбцы.
    """
    X_train, X_test, y_train, y_test = load_data("data/uber.csv")

    # Проверка, что данные не пустые
    assert not X_train.empty, "Данные пустые!"
    assert not X_test.empty, "Данные пустые!"
    assert not y_train.empty, "Целевая переменная пуста!"
    assert not y_test.empty, "Целевая переменная пуста!"

    # Проверка наличия основных колонок в X
    expected_columns = [
        "pickup_longitude", "pickup_latitude",
        "dropoff_longitude", "dropoff_latitude", "passenger_count"
    ]
    for col in expected_columns:
        assert col in X_train.columns, (
            f"Колонка '{col}' отсутствует в X_train!"
        )
