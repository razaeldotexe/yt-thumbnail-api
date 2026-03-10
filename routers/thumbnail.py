from fastapi import APIRouter, Query, HTTPException, Response
from fastapi.responses import FileResponse
import httpx
import os
import tempfile
from schemas.thumbnail import ThumbnailResponse
from utils.url_parser import extract_video_id
from services.yt_service import get_thumbnail_info

router = APIRouter(prefix="/thumbnail", tags=["Thumbnail"])

@router.get("", response_model=ThumbnailResponse)
async def get_thumbnail(
    url: str = Query(..., description="URL video YouTube"),
    cookies: str | None = Query(None, description="Path ke file cookies (opsional)")
):
    """Mengambil metadata dan URL thumbnail dari URL YouTube."""
    video_id = extract_video_id(url)
    if not video_id:
        raise HTTPException(status_code=400, detail="URL YouTube tidak valid atau Video ID tidak ditemukan.")

    try:
        info = await get_thumbnail_info(video_id, cookiefile=cookies)
        return {
            "status": "success",
            "metadata": info["metadata"],
            "thumbnails": info["thumbnails"]
        }
    except Exception as e:
        error_msg = str(e)
        if "Inappropriate content" in error_msg:
            raise HTTPException(status_code=403, detail="Video tidak tersedia atau dibatasi.")
        elif "Video unavailable" in error_msg:
            raise HTTPException(status_code=404, detail="Video tidak ditemukan di YouTube.")
        else:
            raise HTTPException(status_code=500, detail=f"Terjadi kesalahan internal: {error_msg}")

@router.get("/download")
async def download_thumbnail(
    url: str = Query(..., description="URL video YouTube"),
    quality: str = Query("max", enum=["low", "medium", "high", "max"], description="Kualitas thumbnail")
):
    """Mengunduh thumbnail video YouTube secara langsung."""
    video_id = extract_video_id(url)
    if not video_id:
        raise HTTPException(status_code=400, detail="URL YouTube tidak valid.")

    # Pemetaan kualitas ke suffix YouTube
    quality_map = {
        "low": "default",
        "medium": "mqdefault",
        "high": "hqdefault",
        "max": "maxresdefault"
    }
    
    img_url = f"https://img.youtube.com/vi/{video_id}/{quality_map[quality]}.jpg"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(img_url)
            if response.status_code != 200:
                # Fallback ke hqdefault jika maxres tidak ada
                if quality == "max":
                    img_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
                    response = await client.get(img_url)
                
                if response.status_code != 200:
                    raise HTTPException(status_code=404, detail="Thumbnail tidak ditemukan.")

            # Simpan sementara dan kirim sebagai file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
                tmp_file.write(response.content)
                tmp_path = tmp_file.name

            return FileResponse(
                path=tmp_path,
                filename=f"thumbnail_{video_id}.jpg",
                media_type="image/jpeg",
                background=None # FileResponse handle closing
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Gagal mengunduh thumbnail: {str(e)}")
