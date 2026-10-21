"""
Studi kasus: Simulasi klasifikasi risiko banjir.
Dataset sintetis untuk pembelajaran, bukan data hidrologi aktual.
Contoh ini mengadaptasi topik flood forecasting dan disaster response
dari sesi "Bridging Global Infrastructure to Address Local Challenge with HPC".
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


def build_sample_data():
    # Data sintetis: curah hujan (mm/24 jam), tinggi sungai (m), kelembapan (%)
    rows = [
        (10, 0.5, 55), (15, 0.7, 58), (20, 0.8, 60), (25, 0.9, 62),
        (30, 1.0, 65), (35, 1.1, 68), (40, 1.2, 70), (45, 1.3, 72),
        (50, 1.4, 75), (55, 1.5, 78), (60, 1.6, 80), (65, 1.7, 82),
        (70, 1.8, 84), (75, 1.9, 86), (80, 2.0, 88), (85, 2.1, 90),
        (90, 2.2, 91), (95, 2.3, 92), (100, 2.4, 93), (110, 2.5, 94),
        (12, 0.6, 57), (28, 0.9, 63), (38, 1.0, 66), (48, 1.2, 71),
        (58, 1.5, 77), (68, 1.6, 81), (78, 1.8, 85), (88, 2.0, 89),
        (98, 2.2, 92), (105, 2.4, 93), (22, 0.7, 61), (42, 1.1, 69),
        (52, 1.3, 74), (62, 1.5, 79), (72, 1.7, 83), (82, 1.9, 87),
        (92, 2.1, 90), (102, 2.3, 92), (18, 0.6, 59), (33, 1.0, 67),
        (47, 1.2, 73), (57, 1.4, 76), (67, 1.6, 80), (77, 1.8, 84),
        (87, 2.0, 88), (97, 2.2, 91), (107, 2.4, 94), (5, 0.3, 50),
        (115, 2.7, 96), (120, 2.8, 97), (8, 0.4, 52), (72, 1.4, 79),
        (32, 0.8, 64), (83, 2.2, 90), (44, 1.0, 70), (66, 1.8, 85),
        (18, 0.9, 66), (54, 1.7, 82), (101, 2.6, 95), (24, 0.8, 60)
    ]
    df = pd.DataFrame(rows, columns=["curah_hujan_mm", "tinggi_sungai_m", "kelembapan_pct"])

    # Label ilustratif berbasis ambang sederhana untuk membuat contoh terawasi.
    def label_risk(row):
        if row["curah_hujan_mm"] >= 80 or row["tinggi_sungai_m"] >= 2.0:
            return "Tinggi"
        if row["curah_hujan_mm"] >= 40 or row["tinggi_sungai_m"] >= 1.2:
            return "Sedang"
        return "Rendah"

    df["risiko_banjir"] = df.apply(label_risk, axis=1)
    return df


def main():
    data = build_sample_data()
    print("=== SIMULASI KLASIFIKASI RISIKO BANJIR ===")
    print("\nContoh dataset:")
    print(data.head(8).to_string(index=False))
    print(f"\nJumlah data: {len(data)}")
    print("\nJumlah tiap kategori:")
    print(data["risiko_banjir"].value_counts().to_string())

    features = ["curah_hujan_mm", "tinggi_sungai_m", "kelembapan_pct"]
    X = data[features]
    y = data["risiko_banjir"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    model = DecisionTreeClassifier(max_depth=4, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print("\n=== EVALUASI MODEL ===")
    print(f"Data training: {len(X_train)}")
    print(f"Data testing : {len(X_test)}")
    print(f"Accuracy     : {accuracy_score(y_test, predictions):.3f}")
    print("\nClassification report:")
    print(classification_report(y_test, predictions, zero_division=0))
    print("Confusion matrix (urutan kelas mengikuti model):")
    print(confusion_matrix(y_test, predictions))

    new_observation = pd.DataFrame([{
        "curah_hujan_mm": 75,
        "tinggi_sungai_m": 1.8,
        "kelembapan_pct": 86
    }])
    predicted_risk = model.predict(new_observation)[0]

    print("\n=== CONTOH PREDIKSI ===")
    print("Curah hujan 24 jam: 75 mm")
    print("Tinggi sungai     : 1.8 m")
    print("Kelembapan        : 86%")
    print(f"Kategori risiko model: {predicted_risk}")
    print("\nPERINGATAN: ini hanya demonstrasi dengan data sintetis.")
    print("Jangan gunakan hasil ini untuk keputusan evakuasi atau keselamatan nyata.")


if __name__ == "__main__":
    main()
