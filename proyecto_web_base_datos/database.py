from typing import Annotated
from fastapi import Depends
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, sessionmaker
from dotenv import load_dotenv
import os


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./web_app.db")

if DATABASE_URL is None:
    DATABASE_URL = "sqlite:///./web_app.db"

#Crea el motor de la base de datos, es como el puente entre python y la base de datos
#El motor se encarga de gestionar las conexiones y la comunicación con la base de datos
#El argumento connect_args es específico para SQLite y evita problemas con hilos
engine = create_engine(DATABASE_URL, echo=True, connect_args={"check_same_thread": False})  # Solo para SQLite
# engine = create_engine(DATABASE_URL, echo=True)
#Si usas otra base de datos como PostgreSQL o MySQL, no necesitas el argumento connect_args
#Por ejemplo, para PostgreSQL sería:

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Dependencia para obtener la sesión de la base de datos
def get_db():
    with SessionLocal() as session:
        yield session 

DatabaseSession = Annotated[Session, Depends(get_db)]