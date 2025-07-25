from src.data_loader import load_data

# المسار المحلي للملف الجديد
LOCAL_CSV_PATH = "data/uber.csv"

def test_data_loading_from_local_file():
    X_train, X_test, y_train, y_test = load_data(LOCAL_CSV_PATH)

    # Проверка, что данные загружены и не пусты
    assert X_train.shape[0] > 0, "Тренировочная выборка пуста"
    assert X_test.shape[0] > 0, "Тестовая выборка пуста"
    assert X_train.shape[1] == X_test.shape[1], "Количество признаков в train и test не совпадает"
    assert len(y_train) == X_train.shape[0], "Размерности X_train и y_train не совпадают"

    print(
        f"✅ Загружено: {X_train.shape[0]} train, "
        f"{X_test.shape[0]} test, {X_train.shape[1]} признаков"
    )
