from dotenv import load_dotenv
# if your .env is UTF-16 LE:
load_dotenv(encoding='utf-16')

from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import logging
import os

app = FastAPI(
    title="ContentAI API",
    description="AI-powered content generation platform",
    version="1.0.0"
)

# CORS (adjust origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
async def health():
    return {"status": "ok"}

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logging.exception("Unhandled exception")
    return JSONResponse(status_code=500, content={"error": "Internal Server Error", "detail": str(exc)})

# try to include routers if present (non-fatal)
try:
    from routes import content, auth  # adjust if your project uses other names/paths
    app.include_router(content.router, prefix="/api/content")
    app.include_router(auth.router, prefix="/api/auth")
except Exception as e:
    logging.warning("Routers not loaded (continue): %s", e)

# Include other routers
try:
    from routes import brand, campaigns, sponsorship, templates, trending_songs
    app.include_router(brand.router, prefix="/api/brand")
    app.include_router(campaigns.router, prefix="/api/campaigns")
    app.include_router(sponsorship.router, prefix="/api/sponsorship")
    app.include_router(templates.router, prefix="/api/templates")
    app.include_router(trending_songs.router, prefix="/api/trending")
except Exception as e:
    logging.warning("Additional routers not loaded (continue): %s", e)

@app.get("/")
async def root():
    return {"message": "ContentAI API is running"}

@app.get("/api/debug/generate")
async def debug_generate():
    return {"ok": True, "sample_campaign": {"title": "Test Campaign", "body": "This is a generated test."}}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),
        reload=True
    )
