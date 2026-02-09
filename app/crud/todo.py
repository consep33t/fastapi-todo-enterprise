from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func, case
from app.models.todo import Todo, Category
from app.schemas.todo import TodoCreate, TodoUpdate, CategoryCreate

# ==========================================
# BASIC CRUD
# ==========================================

def get_todo(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()

def get_todo_by_name(db: Session, todo_title: str):
    # Mencari berdasarkan title (exact match)
    return db.query(Todo).filter(Todo.title == todo_title).first()

def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Todo).options(joinedload(Todo.category)).offset(skip).limit(limit).all()

def create_todo(db: Session, todo: TodoCreate):
    db_todo = Todo(
        title=todo.title,
        description=todo.description,
        is_completed=todo.is_completed,
        category_id=todo.category_id
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session, db_todo: Todo, todo_update: TodoUpdate):
    update_data = todo_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_todo, key, value)
    
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, db_todo: Todo):
    db.delete(db_todo)
    db.commit()
    return db_todo

# ==========================================
# CATEGORY CRUD
# ==========================================

def create_category(db: Session, category: CategoryCreate):
    db_category = Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Category).offset(skip).limit(limit).all()

def get_category_by_name(db: Session, name: str):
    return db.query(Category).filter(Category.name == name).first()

# ==========================================
# ADVANCED / COMPLEX QUERY
# ==========================================

def get_todos_with_category(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Todo).options(joinedload(Todo.category)).offset(skip).limit(limit).all()

def get_todo_stats(db: Session):
    results = db.query(
        Category.name,
        func.count(Todo.id).label("total_todos"),
        func.sum(case((Todo.is_completed == True, 1), else_=0)).label("completed_todos")
    )\
    .outerjoin(Todo, Category.id == Todo.category_id)\
    .group_by(Category.id)\
    .all()
    
    return [
        {
            "category_name": row[0] if row[0] else "Uncategorized", 
            "total_todos": row[1], 
            "completed_todos": row[2] or 0
        } 
        for row in results
    ]