from pydantic import BaseModel

class ThumbnailURLs(BaseModel):
    """Skema untuk daftar URL thumbnail dengan berbagai resolusi."""
    default: str | None = None
    medium: str | None = None
    high: str | None = None
    max_res: str | None = None

class VideoMetadata(BaseModel):
    """Skema untuk metadata dasar video YouTube."""
    video_id: str
    title: str
    author: str
    description: str | None = None
    duration: int | None = 0  # dalam detik
    view_count: int | None = 0

class ThumbnailResponse(BaseModel):
    """Skema respon lengkap API."""
    status: str
    metadata: VideoMetadata
    thumbnails: ThumbnailURLs
