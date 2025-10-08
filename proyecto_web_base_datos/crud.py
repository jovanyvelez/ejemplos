from sqlalchemy.orm import Session
from sqlalchemy import text

from schemas import UserCreate, ItemCreate

from fastapi import HTTPException

def get_user(db: Session, user_id: int):
    result = db.execute(text("SELECT * FROM users WHERE id = :user_id"), {"user_id": user_id})
    user = result.mappings().first()
    return user if user else None

def get_user_by_email(db: Session, email: str):
    result = db.execute(text("SELECT * FROM users WHERE email = :email"), {"email": email})
    user = result.mappings().first()
    return user if user else None

def get_users(db: Session, skip: int = 0, limit: int = 100):
    result = db.execute(
        text("SELECT * FROM users ORDER BY id LIMIT :limit OFFSET :skip"),
        {"skip": skip, "limit": limit}
    )
    users = result.mappings().all()
    return users

def create_user(db: Session, user: UserCreate):
    # Aquí deberías hashear la contraseña antes de almacenarla
    fake_hashed_password = user.password + "notreallyhashed"
    print("Creating user with email:", user.email)
    db.execute(
        text("""
            INSERT INTO users (email, hashed_password, es_activo) 
            VALUES (:email, :hashed_password, true) 
        """),
        {"email": user.email, "hashed_password": fake_hashed_password}
    )
    db.commit()
    result = db.execute(
        text("SELECT * FROM users WHERE email = :email"),
        {"email": user.email}
    )
    new_user = result.mappings().first()
    return new_user

def create_user_item(db: Session, item: ItemCreate, user_id: int):
    result = db.execute(
        text("""
            INSERT INTO items (nombre, descripcion, propietario_id) 
            VALUES (:nombre, :descripcion, :propietario_id) 
        """),
        {
            "nombre": item.nombre,
            "descripcion": item.descripcion,
            "propietario_id": user_id
        }
    )
    db.commit()
    result = db.execute(
        text("SELECT * FROM items WHERE nombre = :nombre AND propietario_id = :propietario_id"),
        {"nombre": item.nombre, "propietario_id": user_id}
    )
    new_item = result.mappings().first()
    return new_item

def update_user(db: Session, user_id: int, new_email: str):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    result = db.execute(
        text("UPDATE users SET email = :email WHERE id = :user_id"),
        {"email": new_email, "user_id": user_id}
    )
    db.commit()
    updated_user = get_user(db, user_id)
    return updated_user

def deactivate_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.execute(
        text("UPDATE users SET es_activo = false WHERE id = :user_id"),
        {"user_id": user_id}
    )
    db.commit()
    return {"ok": True}

def update_item(db: Session, item_id: int, item: ItemCreate):
    db_item = get_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    result = db.execute(
        text("""
            UPDATE items 
            SET nombre = :nombre, descripcion = :descripcion 
            WHERE id = :item_id 
        """),
        {
            "nombre": item.nombre,
            "descripcion": item.descripcion,
            "item_id": item_id
        }
    )
    db.commit()
    result = db.execute(text("SELECT * FROM items WHERE id = :item_id"), {"item_id": item_id})
    updated_item = result.mappings().first()
    return updated_item

def delete_item(db: Session, item_id: int):
    db_item = get_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.execute(text("DELETE FROM items WHERE id = :item_id"), {"item_id": item_id})
    db.commit()
    return {"ok": True}

def get_items(db: Session, skip: int = 0, limit: int = 100):
    result = db.execute(
        text("SELECT * FROM items ORDER BY id LIMIT :limit OFFSET :skip"),
        {"skip": skip, "limit": limit}
    )
    items = result.mappings().all()
    return items

def get_item(db: Session, item_id: int):
    result = db.execute(text("SELECT * FROM items WHERE id = :item_id"), {"item_id": item_id})
    item = result.mappings().first()
    return item if item else None

def get_items_by_user(db: Session, user_id: int):
    result = db.execute(
        text("SELECT * FROM items WHERE propietario_id = :user_id ORDER BY id"),
        {"user_id": user_id}
    )
    items = result.mappings().all()
    return items