from typing import Annotated

from pydantic import ValidationError

from fastapi import APIRouter, Request, Form, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from models import crear_tablas
from database import DatabaseSession
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles 

from schemas import UserCreate


# Crear las tablas en la base de datos al iniciar la aplicación
# Si las tablas ya existen, no se vuelven a crear
crear_tablas()

router = APIRouter()

templates = Jinja2Templates(directory="templates")



@router.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: DatabaseSession): 
    print(user.model_dump())  
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="El email ya está registrado")
    return crud.create_user(db=db, user=user)

@router.get("/users/", response_model=list[schemas.User])
async def read_users(db: DatabaseSession, skip: int = 0, limit: int = 100):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/users/{user_id}", response_model=schemas.User)
async def read_user(user_id: int, db: DatabaseSession):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.post("/users/{user_id}/items/", response_model=schemas.Item)
async def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: DatabaseSession
):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.create_user_item(db=db, item=item, user_id=user_id)

@router.get("/items/", response_model=list[schemas.Item])
async def read_items(db: DatabaseSession, skip: int = 0, limit: int = 100):
    return crud.get_items(db, skip=skip, limit=limit)

@router.put("/items/{item_id}", response_model=schemas.Item)
async def update_item(item_id: int, item: schemas.ItemCreate, db: DatabaseSession):
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
            raise HTTPException(status_code=404, detail="Item not found")
    return crud.update_item(db=db, item_id=item_id, item=item)  

@router.delete("/items/{item_id}")
async def delete_item(item_id: int, db: DatabaseSession):
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
            raise HTTPException(status_code=404, detail="Item not found")
    return crud.delete_item(db=db, item_id=item_id) 

