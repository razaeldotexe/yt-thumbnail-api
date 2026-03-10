from pydantic import BaseModel

class ThumbnailURLs(BaseModel):
    """Skema untuk daftar URL thumbnail dengan berbagai resolusi."""
    default: str | None = None
    medium: str | None = None
    high: str | None = None
    max_res: str | None = None

class VideoMetadata(BaseModel):
    """Skema untuk metadata dasar video YouTube."""
    title: str
    author: str
    duration: int  # dalam detik

class ThumbnailResponse(BaseModel):
    """Skema respon lengkap API."""
    status: str
    metadata: VideoMetadata
    thumbnails: ThumbnailURLs
