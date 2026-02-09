from typing import List
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Todo API Enterprise"
    DATABASE_URL: str
    
    # TAMBAHAN: Daftar Origin (URL Frontend) yang diizinkan
    # Kita masukkan port umum untuk React (3000), Vite (5173), dan Flutter/Mobile
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost",
        "http://localhost:3000",      # React / Next.js
        "http://localhost:5173",      # Vite (React/Vue)
        "http://localhost:8080",      # Vue / 8080 defaults
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
        # Jika mobile app mengakses via IP local komputer, tambahkan IP komputer Anda (opsional)
        # "http://192.168.1.x:xxxx", 
    ]

    class Config:
        env_file = ".env"

settings = Settings()