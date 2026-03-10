# YT Thumbnail Downloader API 🚀

API berbasis FastAPI untuk mengambil metadata dan mengunduh thumbnail dari video YouTube menggunakan `yt-dlp`.

## ✨ Fitur

- ✅ **URL Parser**: Mendukung berbagai format URL YouTube (Standard, Short, Shorts, YouTube Music, Mobile).
- ✅ **Metadata Video**: Mengambil judul, penulis (uploader), dan durasi video.
- ✅ **Thumbnail Multi-Resolusi**: Menyediakan URL thumbnail resolusi Default (120px), Medium (320px), High (480px), dan Max (1280px).
- ✅ **Download API**: Langsung mengunduh thumbnail sebagai file `.jpg` dengan pilihan kualitas.
- ✅ **Async Implementation**: Dibangun dengan pola asinkronus untuk performa tinggi.

## 🛠️ Tech Stack

- **Python 3.10+**
- **FastAPI** (Web Framework)
- **yt-dlp** (Youtube Metadata Scraper)
- **Uvicorn** (Server)
- **Pydantic** (Data Validation)

## 🚀 Cara Menjalankan

### 1. Kloning Repositori
```bash
git clone <url-repo-anda>
cd yt-thumbnail-api
```

### 2. Instal Dependensi
```bash
pip install -r requirements.txt
```

### 3. Jalankan Server
```bash
uvicorn main:app --reload --port 8080
```
Server akan berjalan di `http://127.0.0.1:8080`.

## 📖 Dokumentasi API

Akses Swagger UI untuk mencoba API secara interaktif:
👉 `http://127.0.0.1:8080/docs`

### Endpoint Utama

#### 1. Get Thumbnail Info
`GET /api/v1/thumbnail`

**Query Param:**
- `url`: URL video YouTube.

**Contoh Response:**
```json
{
  "status": "success",
  "metadata": {
    "title": "Video Title",
    "author": "Channel Name",
    "duration": 300
  },
  "thumbnails": {
    "default": "...",
    "medium": "...",
    "high": "...",
    "max_res": "..."
  }
}
```

#### 2. Download Thumbnail
`GET /api/v1/thumbnail/download`

**Query Param:**
- `url`: URL video YouTube.
- `quality`: (Optional) `low`, `medium`, `high`, atau `max` (Default: `max`).

## 📁 Struktur Proyek

```
yt-thumbnail-api/
├── main.py              # Entry point aplikasi
├── requirements.txt     # Dependensi proyek
├── routers/             # Endpoint API
├── services/            # Logika interaksi yt-dlp
├── schemas/             # Pydantic models (Validasi)
└── utils/               # Helper (URL Parser)
```

## ⚖️ Lisensi

Distribusi bebas untuk tujuan edukasi dan pengembangan.
