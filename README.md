# Flood Risk Classification — HPC-Inspired Study Case

## Overview
Proyek pembelajaran ini membuat simulasi klasifikasi risiko banjir menggunakan
Python dan Decision Tree. Topiknya terinspirasi dari contoh flood forecasting
dan disaster response yang dibahas pada sesi **“Bridging Global Infrastructure
to Address Local Challenge with HPC”** oleh Assistant Professor Dr. Worawan Diaz Carballo.

Proyek ini **bukan sistem prakiraan banjir operasional** dan tidak menggunakan HPC sungguhan.
Ini adalah demonstrasi lokal untuk memahami alur data, pemodelan, evaluasi,
serta bagaimana analisis dapat dikembangkan lebih jauh untuk komputasi berskala besar.

## Tujuan
- Membuat contoh pipeline data untuk masalah risiko banjir.
- Menggunakan fitur curah hujan, tinggi sungai, dan kelembapan.
- Melatih model klasifikasi Decision Tree.
- Mengevaluasi hasil dengan accuracy, precision, recall, F1-score, dan confusion matrix.
- Menghubungkan prototipe lokal dengan gagasan workflow HPC: data → pemrosesan → analisis → hasil.

## Dataset
Dataset dibuat secara sintetis di dalam `main.py`. Label risiko dibentuk menggunakan
ambang ilustratif pada curah hujan dan tinggi sungai.

Fitur:
- `curah_hujan_mm`: curah hujan 24 jam (mm).
- `tinggi_sungai_m`: tinggi sungai (meter).
- `kelembapan_pct`: kelembapan (%).

Target:
- `risiko_banjir`: Rendah, Sedang, atau Tinggi.

## Teknologi
- Python
- Pandas
- Scikit-learn
- Decision Tree Classifier

## Workflow
1. Membuat dan memeriksa data.
2. Memisahkan fitur dan label.
3. Membagi data menjadi training dan testing.
4. Melatih model Decision Tree.
5. Menghasilkan prediksi.
6. Mengevaluasi menggunakan accuracy, classification report, dan confusion matrix.

## Cara menjalankan di Windows
Buat virtual environment:
```bash
python -m venv .venv
```

Aktifkan di PowerShell:
```powershell
.venv\\Scripts\\Activate.ps1
```

Atau gunakan Command Prompt:
```bat
.venv\\Scripts\\activate.bat
```

Instal library dan jalankan:
```bash
python -m pip install -r requirements.txt
python main.py
```

## Hubungan dengan HPC
Proyek ini berjalan pada komputer lokal dan tidak mengakses supercomputer. Untuk skala lebih besar,
pipeline serupa dapat dikembangkan dengan data sensor/stasiun cuaca yang tervalidasi, pemrosesan
paralel, job scheduler, serta infrastruktur HPC sebagaimana workflow umum yang dijelaskan dalam sesi.

## Keterbatasan dan keselamatan
Data sintetis dan aturan label hanya untuk demonstrasi. Model tidak divalidasi terhadap kejadian banjir
sebenarnya dan tidak boleh dipakai untuk peringatan, evakuasi, atau keputusan keselamatan. Implementasi
nyata membutuhkan data historis resmi, kalibrasi sensor, evaluasi ahli hidrologi, validasi menyeluruh,
dan sistem operasional yang dapat dipercaya.

## Author
Afifah Chairunnisya
