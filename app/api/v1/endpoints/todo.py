from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

# Import Schemas
from app.schemas.todo import (
    TodoCreate, 
    TodoResponse, 
    TodoUpdate, 
    TodoStatistics,
    CategoryCreate, 
    CategoryResponse
)
# Import CRUD
from app.crud import todo as crud_todo
# Import DB Session
from app.db.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1. CREATE TODO (POST)
@router.post("/", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    return crud_todo.create_todo(db=db, todo=todo)

# 2. READ ALL TODOS (GET)
@router.get("/", response_model=List[TodoResponse])
def read_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_todo.get_todos(db, skip=skip, limit=limit)

# ==========================================
# ENDPOINT KATEGORI
# ==========================================
@router.post("/categories", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    # 1. Cek apakah kategori sudah ada
    category_exists = crud_todo.get_category_by_name(db, name=category.name)
    if category_exists:
        raise HTTPException(
            status_code=400, # Bad Request
            detail="Category with this name already exists"
        )
    return crud_todo.create_category(db=db, category=category)

@router.get("/categories", response_model=List[CategoryResponse])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_todo.get_categories(db, skip=skip, limit=limit)

# =================================================================
# 3. STATS (GET) -- STATIC PATHS (Harus di atas Dynamic ID)
# =================================================================
@router.get("/stats", response_model=List[TodoStatistics])
def read_stats(db: Session = Depends(get_db)):
    return crud_todo.get_todo_stats(db)

# =================================================================
# PENCARIAN TITLE (GET BY TITLE)
# PENTING: Gunakan prefix "/title/" agar tidak bentrok dengan ID
# =================================================================
@router.get("/title/{todo_title}", response_model=TodoResponse)
def read_todo_by_title(todo_title: str, db: Session = Depends(get_db)):
    db_todo = crud_todo.get_todo_by_name(db, todo_title=todo_title)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found by title")
    return db_todo

# =================================================================
# 4. READ ONE (GET BY ID) -- DYNAMIC PATHS (Taruh paling bawah)
# =================================================================
@router.get("/{todo_id}", response_model=TodoResponse)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud_todo.get_todo(db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

# 5. UPDATE (PUT)
@router.put("/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, todo_in: TodoUpdate, db: Session = Depends(get_db)):
    db_todo = crud_todo.get_todo(db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return crud_todo.update_todo(db=db, db_todo=db_todo, todo_update=todo_in)

# 6. DELETE (DELETE)
@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud_todo.get_todo(db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    crud_todo.delete_todo(db=db, db_todo=db_todo)
    return None