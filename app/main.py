from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # <--- Import ini

from app.api.v1.endpoints import todo
from app.core.config import settings

# Inisialisasi App
app = FastAPI(title=settings.PROJECT_NAME)

# -----------------------------------------------------------------------
# KONFIGURASI CORS (Enterprise Standard)
# -----------------------------------------------------------------------
# Jika settings.BACKEND_CORS_ORIGINS ada isinya, pasang middleware
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        # Mengizinkan origin yang terdaftar di config
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        # Mengizinkan kredensial (cookies, authorization headers)
        allow_credentials=True,
        # Mengizinkan semua method (GET, POST, PUT, DELETE, OPTIONS, dll)
        allow_methods=["*"],
        # Mengizinkan semua header (Content-Type, Authorization, dll)
        allow_headers=["*"],
    )
# -----------------------------------------------------------------------

# Include Router (Grouping)
app.include_router(todo.router, prefix="/api/v1/todos", tags=["todos"])

@app.get("/")
def root():
    return {"message": "Welcome to Enterprise FastAPI Todo API"}