from src.data_loader import load_data

LOCAL_CSV_PATH = "data/uber.csv"

def test_data_loading_from_local_file():
    X_train, X_test, y_train, y_test = load_data(LOCAL_CSV_PATH)

    assert not X_train.empty, "❌ X_train فاضي!"
    assert not X_test.empty, "❌ X_test فاضي!"
    assert len(X_train) == len(y_train), "❌ X_train و y_train مش متطابقين في الحجم!"
    assert X_train.shape[1] == X_test.shape[1], "❌ عدد الأعمدة في X_train و X_test مختلف!"
    
    print("✅ تم تحميل وتقسيم البيانات بنجاح")
