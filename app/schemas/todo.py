from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import datetime

# =======================
# CATEGORY SCHEMAS
# =======================
class CategoryBase(BaseModel):
    # Hapus 'id' dari sini agar tidak muncul saat Create
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int

    # Config untuk Pydantic V2 (Support ORM reading)
    model_config = ConfigDict(from_attributes=True)

# =======================
# TODO SCHEMAS
# =======================
class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    is_completed: bool = False
    # Optional karena user bisa buat todo tanpa kategori (Uncategorized)
    category_id: Optional[int] = None 

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    # Semua field Optional untuk mendukung Partial Update (PATCH)
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None
    category_id: Optional[int] = None

class TodoResponse(TodoBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    # Nested Object: Menampilkan detail kategori lengkap, bukan cuma ID
    category: Optional[CategoryResponse] = None 

    # Config untuk Pydantic V2
    model_config = ConfigDict(from_attributes=True)

# =======================
# STATISTICS SCHEMAS
# =======================
class TodoStatistics(BaseModel):
    category_name: str
    total_todos: int
    completed_todos: int