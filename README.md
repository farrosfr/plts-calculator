# ☀️ PLTS Pro Calculator

Sebuah aplikasi kalkulator berbasis command-line yang dirancang secara modular untuk membantu memperkirakan kebutuhan komponen utama dalam sistem Pembangkit Listrik Tenaga Surya (PLTS) tipe *off-grid*.

## ✨ Fitur Utama

- **Kalkulasi Komprehensif**: Menghitung 3 komponen inti PLTS:
  - Total Kapasitas Panel Surya (Watt-peak)
  - Total Kapasitas Baterai (Ampere-hour)
  - Ukuran Minimum Solar Charge Controller (Ampere)
- **Dua Mode Input Beban**:
  1.  **Mode Daftar Alat**: Menghitung total beban harian secara interaktif dengan memilih dari daftar peralatan listrik yang umum.
  2.  **Mode Manual**: Memasukkan total kebutuhan energi harian (Watt-hour) secara langsung.
- **Struktur Modular**: Kode dipecah menjadi beberapa modul dengan tanggung jawab yang jelas, membuatnya mudah dipahami, dipelihara, dan dikembangkan lebih lanjut.
- **Data Dinamis**: Daftar peralatan listrik disimpan dalam file `JSON` sehingga mudah untuk ditambah atau diubah tanpa menyentuh kode utama.

## 📂 Struktur Proyek

Proyek ini dirancang dengan prinsip pemisahan logika untuk keterbacaan dan skalabilitas yang lebih baik.

```

plts\_pro\_calculator/
├── main.py                     \# Titik masuk utama aplikasi
├── modules/
│   ├── **init**.py             \# Membuat 'modules' menjadi sebuah package Python
│   ├── input\_handler.py        \# Mengelola semua input dari pengguna
│   ├── calculator.py           \# Berisi semua logika dan rumus perhitungan
│   └── display.py                \# Mengatur semua output yang ditampilkan ke pengguna
└── data/
└── appliance\_wattage.json    \# Menyimpan data daya (watt) peralatan umum

````

## 🚀 Cara Menjalankan

Untuk menjalankan aplikasi ini di komputer Anda, ikuti langkah-langkah berikut:

**1. Prasyarat**
- Pastikan Anda sudah menginstal **Python 3.x**.

**2. Instalasi**
- Clone repositori ini ke komputer lokal Anda:
  ```bash
  git clone https://github.com/farrosfr/plts-calculator.git
  ````

*(Jangan lupa ganti `your-username` dengan username GitHub Anda)*

  - Masuk ke direktori proyek:
    ```bash
    cd plts-calculator
    ```

**3. Jalankan Aplikasi**

  - Eksekusi file `main.py` menggunakan Python:
    ```bash
    python main.py
    ```
  - Aplikasi akan berjalan di terminal Anda dengan menu interaktif.

## 💡 Kustomisasi

Anda dapat dengan mudah menambahkan atau mengubah daftar peralatan listrik dengan mengedit file `data/appliance_wattage.json`. Cukup ikuti format JSON yang sudah ada.

```json
[
  { "nama": "Nama Alat Baru", "watt": 100 },
  ...
]
```

## 🤝 Kontribusi

Saran dan kontribusi sangat diterima. Jika Anda memiliki ide untuk perbaikan, silakan buat *Fork* dari repositori ini dan ajukan *Pull Request*.