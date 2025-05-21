import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_class_distribution(data: pd.DataFrame) -> None:
    """
    Membuat visualisasi distribusi kelas dalam dataset
    Args:
        data: DataFrame yang berisi data mobil
    """
    plt.figure(figsize=(8, 6))
    sns.countplot(data=data, x='class', palette='Set2')
    plt.title('Distribusi Kelas pada Dataset Car Evaluation')
    plt.xlabel('Kelas')
    plt.ylabel('Jumlah')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_safety_vs_class(data: pd.DataFrame) -> None:
    """
    Membuat visualisasi hubungan antara tingkat keamanan dan kelas mobil
    Args:
        data: DataFrame yang berisi data mobil
    """
    crosstab = pd.crosstab(data['safety'], data['class'], normalize='index')
    plt.figure(figsize=(8, 5))
    sns.heatmap(crosstab, annot=True, cmap='YlGnBu', fmt=".2f")
    plt.title("Distribusi Kelas Berdasarkan Tingkat Keamanan")
    plt.ylabel("Tingkat Keamanan")
    plt.xlabel("Kelas Mobil")
    plt.tight_layout()
    plt.show()

def plot_correlation(data: pd.DataFrame) -> None:
    plt.figure(figsize=(10, 6))
    sns.set(font_scale=1.2)
    sns.heatmap(df.corr(), annot=True, cmap='rainbow', linewidth=0.5)
    plt.title('Correlation Matrix')
    plt.tight_layout()
    plt.show()
