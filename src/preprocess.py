import pandas as pd
from pandas.api.types import CategoricalDtype

def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Memproses data mentah dari UCI ML Repository menjadi format yang siap digunakan untuk training
    
    Args:
        data: DataFrame mentah yang berisi data evaluasi mobil
        
    Returns:
        DataFrame yang sudah diproses dengan fitur kategorikal diubah menjadi numerik
    """
    # Mendefinisikan tipe data kategorikal untuk setiap fitur
    # ordered=True karena nilai kategori memiliki urutan tingkatan
    buying_type = CategoricalDtype(['low','med','high','vhigh'], ordered=True)  # Tingkat harga pembelian
    maint_type = CategoricalDtype(['low','med','high','vhigh'], ordered=True)   # Tingkat biaya perawatan
    doors_type = CategoricalDtype(['2','3','4','5more'], ordered=True)          # Jumlah pintu
    persons_type = CategoricalDtype(['2','4','more'], ordered=True)             # Kapasitas penumpang
    lug_boot_type = CategoricalDtype(['small','med','big'], ordered=True)       # Ukuran bagasi
    safety_type = CategoricalDtype(['low','med','high'], ordered=True)          # Tingkat keamanan
    class_type = CategoricalDtype(['unacc','acc','good','vgood'], ordered=True) # Kelas evaluasi mobil

    # Mengubah tipe data menjadi kategorikal
    data['buying'] = data['buying'].astype(buying_type)
    data['maint'] = data['maint'].astype(maint_type)
    data['doors'] = data['doors'].astype(doors_type)
    data['persons'] = data['persons'].astype(persons_type)
    data['lug_boot'] = data['lug_boot'].astype(lug_boot_type)
    data['safety'] = data['safety'].astype(safety_type)
    data['class'] = data['class'].astype(class_type)

    # Mengubah data kategorikal menjadi kode numerik
    # Kode akan sesuai dengan urutan kategori yang didefinisikan di atas
    data['buying'] = data['buying'].cat.codes     # 0:low, 1:med, 2:high, 3:vhigh
    data['maint'] = data['maint'].cat.codes       # 0:low, 1:med, 2:high, 3:vhigh
    data['doors'] = data['doors'].cat.codes       # 0:2, 1:3, 2:4, 3:5more
    data['persons'] = data['persons'].cat.codes   # 0:2, 1:4, 2:more
    data['lug_boot'] = data['lug_boot'].cat.codes # 0:small, 1:med, 2:big
    data['safety'] = data['safety'].cat.codes     # 0:low, 1:med, 2:high
    data['class'] = data['class'].cat.codes       # 0:unacc, 1:acc, 2:good, 3:vgood

    # Memastikan semua data bertipe numerik
    # errors='coerce' akan mengubah nilai yang tidak bisa dikonversi menjadi NaN
    data = data.apply(pd.to_numeric, errors='coerce')
    
    return data
