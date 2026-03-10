# YT Thumbnail Downloader API

API production-ready untuk mengambil metadata dan mengunduh thumbnail dari YouTube menggunakan Python, FastAPI, dan `yt-dlp`.

## 🚀 Fitur Utama

- **Ekstraksi Metadata**: Judul video, nama uploader, dan durasi.
- **Dukungan URL Luas**: Mendukung URL YouTube standar, Short (`youtu.be`), Shorts, YouTube Music, dan Mobile.
- **Resolusi Beragam**: Menyediakan link thumbnail untuk resolusi Default, Medium, High, hingga Max Resolution.
- **Direct Download**: Endpoint khusus untuk mengunduh file thumbnail langsung ke komputer.
- **Async & Performance**: Dibangun secara asinkron dengan FastAPI untuk performa tinggi.

## 🛠️ Tech Stack

- Python 3.10+
- FastAPI
- yt-dlp
- Uvicorn
- Pydantic
- Httpx

## 📋 Persyaratan

Pastikan Anda memiliki Python 3.10 atau versi yang lebih baru terinstal di sistem Anda.

## ⚙️ Instalasi

1. Clone repositori ini atau download source code-nya.
2. Instal dependensi menggunakan pip:
   ```bash
   pip install -r requirements.txt
   ```

## 🏃 Menjalankan API

Jalankan server menggunakan Uvicorn:
```bash
uvicorn main:app --reload --port 8080
```
*Catatan: Gunakan port `8080` jika port `8000` sudah digunakan oleh proses lain.*

## 📖 Dokumentasi API

Setelah server berjalan, Anda dapat mengakses dokumentasi interaktif (Swagger UI) di:
- **Dokumentasi**: [http://127.0.0.1:8080/docs](http://127.0.0.1:8080/docs)

## 📡 Endpoint Utama

### 1. Dapatkan Metadata & URL Thumbnail
**GET** `/api/v1/thumbnail`

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `url` | `string` | **Required**. URL video YouTube |

**Contoh Request:**
`http://127.0.0.1:8080/api/v1/thumbnail?url=https://www.youtube.com/watch?v=dQw4w9WgXcQ`

---

### 2. Download Thumbnail Langsung
**GET** `/api/v1/thumbnail/download`

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `url` | `string` | **Required**. URL video YouTube |
| `quality` | `string` | **Optional**. Pilihan: `low`, `medium`, `high`, `max` (Default: `max`) |

**Contoh Request:**
`http://127.0.0.1:8080/api/v1/thumbnail/download?url=https://youtu.be/dQw4w9WgXcQ&quality=max`

## 📂 Struktur Project

```text
yt-thumbnail-api/
├── main.py              # Entry point FastAPI
├── requirements.txt     # Daftar dependensi
├── routers/             # Endpoint API
├── services/            # Logika integrasi yt-dlp
├── schemas/             # Validasi data Pydantic
└── utils/               # Fungsi pembantu (URL Parser)
```

## 📝 Lisensi
Bebas digunakan untuk keperluan belajar maupun komersial.
