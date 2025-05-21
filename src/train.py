import pickle
from data_loader import load_data
from preprocess import preprocess_data
from models import get_decision_tree_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

def train():
    # Memuat dan memproses data dari UCI ML Repository (ID: 19)
    data = preprocess_data(load_data(19))

    # Memisahkan fitur (features) dan target (class)
    features = data.drop('class', axis=1)  # Mengambil semua kolom kecuali 'class'
    target = data['class']  # Mengambil kolom 'class' sebagai target

    # Membagi data menjadi data training (80%) dan testing (20%)
    features_train, _, target_train, _ = train_test_split(features, target, test_size=0.2, random_state=42)

    # Melakukan standarisasi fitur menggunakan StandardScaler
    scaler = StandardScaler()
    features_train_scaled = scaler.fit_transform(features_train)

    # Mengatasi imbalanced data menggunakan SMOTE
    smote = SMOTE(random_state=42)
    features_train_resampled, target_train_resampled = smote.fit_resample(features_train_scaled, target_train)    

    # Membuat dan melatih model decision tree
    model = get_decision_tree_model()
    model.fit(features_train_resampled, target_train_resampled)

    # Menyimpan model yang sudah dilatih
    with open("../save_models/model.pkl", "wb") as f:
        pickle.dump(model, f)

    # Menyimpan scaler untuk standarisasi fitur
    with open("../save_models/scaler.pkl", "wb") as f:
        pickle.dump(scaler, f)

if __name__ == '__main__':
    train()
