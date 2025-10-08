from fastapi import FastAPI

from models import crear_tablas
from users import router as users

crear_tablas()

app = FastAPI(title="Ejemplo API con FastAPI y SQLAlchemy", 
              version="0.1.0", 
              description="Un ejemplo simple de una API con FastAPI y SQLAlchemy para mostrar conexión a base de datos y operaciones CRUD"
              )


app.include_router(users)
