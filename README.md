# Bike rental Dashboard
Dashboard ini dirancang untuk menganalisis data peminjaman sepeda berdasarkan faktor cuaca dan waktu. Menggunakan Streamlit, Pandas, Seaborn, dan Matplotlib untuk menyajikan berbagai visualisasi yang membantu dalam memahami pola penggunaan sepeda.

Cara Menjalankan Dashboard

-Persyaratan-

Sebelum menjalankan dashboard, pastikan Anda telah menginstal:

Python (>=3.7)

Streamlit

Pandas

Matplotlib

Seaborn

NumPy

```bash 
pip install streamlit pandas matplotlib seaborn numpy

 Menjalankan Dashboard

Simpan script Python dashboard (dashboard.py).

Buka terminal atau command prompt.

Arahkan ke direktori tempat file disimpan.

Jalankan perintah berikut:
streamlit run dashboard.py

Dashboard akan terbuka di browser secara otomatis.



-Upload Dataset-

Dashboard memerlukan dua file CSV:

day.csv: Berisi data peminjaman sepeda per hari.

hour.csv: Berisi data peminjaman sepeda per jam.

Cara upload:

Klik tombol Browse files pada bagian "Upload Data Files".

Pilih file day.csv dan hour.csv.

Data akan otomatis ditampilkan jika format sesuai.



-Fitur Dashboard-

1️⃣ Preview Dataset

Menampilkan 5 baris pertama dari day.csv dan hour.csv untuk memastikan data terupload dengan benar.

2️⃣ Weather Condition Overview 🌦️

Menampilkan kondisi cuaca dalam bentuk teks berdasarkan kolom weathersit.

3️⃣ Daily Bike Rental Trends 📅

Visualisasi jumlah peminjaman sepeda per hari menggunakan line chart.

4️⃣ Hourly Bike Rental Trends 🕒

Visualisasi jumlah peminjaman sepeda per jam dalam satu hari menggunakan line chart.

5️⃣ Heatmap: Bike Rentals by Hour and Weekday 🔥

Menampilkan jumlah peminjaman sepeda berdasarkan jam dan hari dalam seminggu menggunakan heatmap.

6️⃣ Weather Factors vs Bike Rentals 🌡️

Scatter plot hubungan antara suhu dan jumlah peminjaman sepeda.

7️⃣ User Distribution by Weather Condition ☁️

Histogram distribusi jumlah pengguna berdasarkan kondisi cuaca.

8️⃣ Casual vs Registered Users 👥

Menampilkan pie chart perbandingan pengguna kasual dan pengguna terdaftar.

9️⃣ Bike Rentals: Workday vs Weekend 📆

Bar chart membandingkan jumlah peminjaman sepeda pada hari kerja vs akhir pekan.

Dashboard ini membantu dalam memahami pola peminjaman sepeda berdasarkan faktor cuaca dan waktu. Dengan visualisasi yang interaktif, pengguna dapat menganalisis tren peminjaman dan membuat keputusan berdasarkan data.
