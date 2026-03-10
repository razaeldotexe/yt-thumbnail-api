from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import thumbnail

app = FastAPI(
    title='YT Thumbnail Downloader API',
    description='API sederhana untuk mengambil metadata dan mengunduh thumbnail dari video YouTube.',
    version='1.0.0',
    docs_url='/docs'
)

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Router
app.include_router(thumbnail.router, prefix="/api/v1")

@app.get("/", tags=["Root"])
async def root():
    """Endpoint utama aplikasi."""
    return {
        "message": "Welcome to YT Thumbnail Downloader API",
        "docs": "/docs",
        "status": "online"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
