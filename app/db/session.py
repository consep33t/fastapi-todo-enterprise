from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# engine: Mesin utama koneksi
engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)

# SessionLocal: Factory untuk membuat session database di setiap request
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)