# LISA Purwokerto

Merupakan aplikasi yang digunakan untuk sarana informasi masyarakat terkait KPw Bank Indonesia Purwokerto. Aplikasi ini terinsipirasi oleh Chatbot LISA dari Bank Indonesia yang bisa diakses melalui WhatsApp.
Aplikasi ini bisa diakses di link berikut : https://lisa-purwokerto.streamlit.app/

## Prerequisites

Sebelum memulai, pastikan Anda telah menginstal Python (versi 3.7 atau lebih baru). Anda dapat memeriksa versi Python yang terinstal dengan menjalankan perintah berikut di terminal atau command prompt:

```bash
python --version
```

Jika Python belum terinstal, Anda dapat mengunduhnya dari [situs resmi Python](https://www.python.org/downloads/).

## Instalasi

1. **Buka folder proyek**  
   Gunakan terminal atau command prompt untuk membuka folder tempat aplikasi Anda disimpan. Misalnya:

   ```bash
   cd path/to/your/project
   ```

2. **Pasang library yang diperlukan**  
   Pastikan Anda memiliki `pip` terinstal. Kemudian, jalankan perintah berikut untuk menginstal semua dependensi yang tercantum di `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

## Menjalankan Aplikasi

Setelah semua library terpasang, Anda dapat menjalankan aplikasi dengan perintah berikut:

```bash
streamlit run main.py
```

Aplikasi akan terbuka di browser Anda secara otomatis. Jika tidak, Anda dapat mengaksesnya di [http://localhost:8501](http://localhost:8501).



# Tutorial Mengupload Aplikasi ke Streamlit Share

Panduan ini menjelaskan langkah-langkah untuk mengupload aplikasi Streamlit Anda ke Streamlit Share agar dapat diakses secara online.

## Prerequisites

Sebelum memulai, pastikan Anda memiliki hal-hal berikut:

1. **Akun GitHub**: Anda perlu akun GitHub untuk menyimpan kode aplikasi Anda.
2. **Aplikasi Streamlit**: Pastikan Anda sudah memiliki aplikasi Streamlit yang siap untuk diupload.

## Langkah-Langkah Mengupload Aplikasi

### 1. Siapkan Repositori di GitHub

- Masuk ke akun GitHub Anda.
- Buat repositori baru dengan mengklik tombol "New" di halaman repositori.
- Beri nama repositori sesuai dengan nama aplikasi Anda dan pilih opsi "Public".

### 2. Upload Kode Aplikasi

1. Clone repositori yang baru saja Anda buat ke komputer lokal Anda:

   ```bash
   git clone https://github.com/username/nama-repositori.git
   ```

   Gantilah `username` dengan username GitHub Anda dan `nama-repositori` dengan nama repositori yang telah dibuat.

2. Salin semua file aplikasi Streamlit Anda (termasuk `main.py` dan `requirements.txt`) ke dalam folder repositori yang telah Anda clone.

3. Tambahkan dan commit perubahan:

   ```bash
   git add .
   git commit -m "Initial commit"
   ```

4. Push perubahan ke GitHub:

   ```bash
   git push origin main
   ```

### 3. Deploy di Streamlit Share

1. Buka [Streamlit Share](https://share.streamlit.io/).
2. Masuk dengan akun GitHub Anda.
3. Klik tombol "New app".
4. Pilih repositori yang Anda buat sebelumnya.
5. Pada kolom "Main file path", masukkan nama file utama Anda, misalnya `main.py`.
6. Klik tombol "Deploy".

Aplikasi Anda akan di-build dan segera tersedia di URL yang disediakan oleh Streamlit Share. Tunggu beberapa saat hingga proses selesai.

### 4. Akses Aplikasi

Setelah aplikasi berhasil di-deploy, Anda akan diberikan URL untuk mengakses aplikasi Anda secara online. Anda dapat membagikan URL tersebut kepada orang lain.

## Troubleshooting

- **Kesalahan Dependensi**: Pastikan `requirements.txt` Anda sudah lengkap dengan semua library yang diperlukan.
- **Error di Build**: Periksa log yang ditampilkan di Streamlit Share untuk mendapatkan informasi lebih lanjut tentang kesalahan yang terjadi.
