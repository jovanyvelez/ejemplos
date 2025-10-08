
from pydantic import BaseModel, EmailStr, field_validator

from datetime import datetime



class ItemBase(BaseModel):
    nombre: str
    descripcion: str | None = None  

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    propietario_id: int

    class Config:
        orm_mode = True #Para que Pydantic pueda trabajar con objetos ORM de SQLAlchemy  


class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

    @field_validator('password')
    def password_length(cls, value):
        if len(value) < 8:
            raise ValueError('La contraseña debe tener al menos 8 caracteres.')
        return value
    
class User(UserBase):
    id: int
    es_activo: bool
    created_at: datetime
    items: list[Item] = []

    class Config:
        orm_mode = True  #Para que Pydantic pueda trabajar con objetos ORM de SQLAlchemy