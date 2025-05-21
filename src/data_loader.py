from ucimlrepo import fetch_ucirepo
import pandas as pd

def load_data(dataset_id: int) -> pd.DataFrame:
    """
    Mengambil dataset Car Evaluation dari UCI ML Repository
    Args:
        dataset_id: ID dataset di UCI ML Repository (19 untuk Car Evaluation)
    Returns:
        pd.DataFrame: DataFrame yang berisi data mentah
    """
    # Mengambil data dari UCI ML Repository
    data = fetch_ucirepo(id=dataset_id)
    
    # Mengambil data original (belum diproses)
    return data.data['original']
