from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
import graphviz

def get_decision_tree_model(random_state=42):
    """
    Membuat model Decision Tree Classifier
    Args:
        random_state: Nilai seed untuk reproduksibilitas hasil
    Returns:
        DecisionTreeClassifier: Model decision tree yang siap digunakan
    """
    return DecisionTreeClassifier(random_state=random_state)

def visualize_tree(model, feature_names, class_names):
    """
    Memvisualisasikan pohon keputusan
    Args:
        model: Model decision tree yang sudah dilatih
        feature_names: Nama-nama fitur yang digunakan
        class_names: Nama-nama kelas target
    Returns:
        graphviz.Source: Objek visualisasi pohon keputusan
    """
    # Mengekspor pohon keputusan ke format DOT
    dot_data = export_graphviz(model, out_file=None,
                              feature_names=feature_names,
                              class_names=class_names,
                              filled=True, rounded=True,
                              special_characters=True)
    
    # Membuat visualisasi dengan graphviz
    graph = graphviz.Source(dot_data)
    graph.render("decision_tree", format="png", view=True)
    return graph


def get_decision_tree_model(random_state=42):
    return DecisionTreeClassifier(random_state=random_state)

