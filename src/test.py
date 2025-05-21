import pickle
from data_loader import load_data
from preprocess import preprocess_data
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

def evaluate():
    # Memuat dan memproses data dari UCI ML Repository (ID: 19)
    data = preprocess_data(load_data(19))

    # Memisahkan fitur (features) dan target (class)
    features = data.drop('class', axis=1)  # Mengambil semua kolom kecuali 'class'
    target = data['class']  # Mengambil kolom 'class' sebagai target

    # Membagi data menjadi data training (80%) dan testing (20%)
    _, features_test, _, target_test = train_test_split(features, target, test_size=0.2, random_state=42)

    # Memuat model yang sudah dilatih
    with open("../save_models/model.pkl", "rb") as f:
        model = pickle.load(f)

    # Memuat scaler untuk standarisasi fitur
    with open("../save_models/scaler.pkl", "rb") as f:
        scaler = pickle.load(f)

    # Melakukan standarisasi pada data test
    features_test_scaled = scaler.transform(features_test)
    
    # Melakukan prediksi menggunakan model
    target_pred = model.predict(features_test_scaled)

    # Menampilkan hasil evaluasi
    print("Accuracy:", accuracy_score(target_test, target_pred))
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

if __name__ == '__main__':
    evaluate()
