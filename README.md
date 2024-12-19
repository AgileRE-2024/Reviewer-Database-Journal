# Reviewer-Database-Journal
Aplikasi "Reviewer Database Journal" adalah aplikasi berbasis Django yang dirancang untuk membantu editor dari sebuah paper untuk menemukan rekomendasi reviewer yang cocok untuk paper mereka. Berikut adalah langkah-langkah untuk menginstal dan menjalankan aplikasi ini.

---

## Prasyarat

Sebelum memulai instalasi, pastikan Anda sudah memiliki:

1. **Python** versi 3.8 atau lebih baru.
2. **Git** untuk meng-clone repositori.
3. **Pip** (Package Installer for Python).

---

## Langkah Instalasi

### 1. Clone Repositori dari GitHub

1. Buka terminal atau command prompt.
2. Jalankan perintah berikut untuk meng-clone repositori aplikasi:
   ```bash
   git clone https://github.com/AgileRE-2024/Reviewer-Database-Journal.git
   ```

### 2. Instal Dependensi

Jalankan perintah berikut untuk menginstal dependensi yang dibutuhkan aplikasi:
```bash
pip install -r requirements.txt
```

### 3. Membuka Direktori Aplikasi

1. Masuk ke direktori proyek:
   ```bash
   cd mysite
   ```

### 4. Migrasi Database

1. Jalankan perintah migrasi untuk membuat tabel di database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

### 5. Buat Superuser

Untuk mengakses halaman admin, buat superuser dengan perintah berikut:
```bash
python manage.py createsuperuser
```
Ikuti instruksi untuk mengisi username, email, dan password.

### 6. Jalankan Server Lokal

Jalankan server pengembangan Django dengan perintah berikut:
```bash
python manage.py runserver
```

Akses aplikasi di browser Anda di alamat berikut:
```
http://127.0.0.1:8000
```

---

