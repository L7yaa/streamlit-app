# Bike rental Dashboard
Fitur

Upload File CSV: Mengunggah file day.csv dan hour.csv.

Preview Dataset: Menampilkan 5 baris pertama dari dataset harian dan per jam.

Visualisasi Data:

Boxplot penyewaan sepeda berdasarkan kondisi cuaca.

Grafik garis jumlah total penyewaan berdasarkan jam dalam sehari.

Heatmap korelasi antar variabel.

Keterangan Cuaca: Menampilkan arti kode cuaca dari dataset.

Persyaratan

Sebelum menjalankan aplikasi, pastikan sistem Anda memiliki:

Python 3.7 atau lebih baru

Paket Python yang diperlukan:

pandas

matplotlib

seaborn

streamlit

Untuk menginstal semua dependensi, jalankan perintah berikut:

pip install pandas matplotlib seaborn streamlit

Cara Menjalankan Dashboard

Clone atau Unduh Repositori

git clone https://github.com/username/bike-rental-dashboard.git
cd bike-rental-dashboard

Jalankan Streamlit

streamlit run dashboard.py

Unggah File Data

day.csv: Data penyewaan sepeda harian

hour.csv: Data penyewaan sepeda per jam

Eksplorasi Data & Visualisasi

Lihat preview dataset

Analisis tren penyewaan berdasarkan cuaca dan waktu

Struktur Direktori

📂 bike-rental-dashboard
 ├── 📄 dashboard.py         # Kode utama aplikasi Streamlit
 ├── 📄 README.md            # Dokumentasi
 ├── 📂 data                 # Direktori untuk menyimpan dataset (opsional)
 ├── 📄 requirements.txt      # Daftar dependensi (opsional)

Penjelasan Kode Cuaca

Dataset weathersit memiliki kode berikut:

1 = Cuaca Cerah / Berawan Ringan

2 = Kabut + Berawan / Mendung

3 = Hujan Ringan / Salju Ringan

4 = Hujan Lebat / Salju Lebat / Badai

Pastikan Anda mengunggah file CSV dengan format yang sesuai agar dashboard berjalan dengan baik. 🚴‍♂️
