from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
    
    # Relasi ke Todo (Satu kategori punya banyak todo)
    todos = relationship("Todo", back_populates="category")

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True)
    description = Column(String(255), nullable=True)
    is_completed = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # --- TAMBAHAN RELASI ---
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    
    # Relasi balik ke Category (Lazy='joined' agar otomatis di-load saat query)
    category = relationship("Category", back_populates="todos")