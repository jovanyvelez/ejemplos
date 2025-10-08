# Crear las tablas usando SQL raw con text() al importar el módulo
from sqlalchemy import text
from sqlalchemy.orm import Session
from database import engine

def crear_tablas():
    with Session(engine) as session:
        session.execute(text("""
            CREATE TABLE IF NOT EXISTS "users" (
                "id" INTEGER NOT NULL,
                "email" VARCHAR NOT NULL,
                "hashed_password" VARCHAR NOT NULL,
                "es_activo" BOOLEAN NOT NULL,
                "created_at" DATETIME NOT NULL DEFAULT (datetime('now')),
                PRIMARY KEY("id")
            );
        """))
        session.execute(text("""
            CREATE TABLE IF NOT EXISTS "items" (
                "id" INTEGER NOT NULL,
                "nombre" VARCHAR NOT NULL,
                "descripcion" VARCHAR,
                "created_at" DATETIME NOT NULL DEFAULT (datetime('now')),
                "propietario_id" INTEGER,
                PRIMARY KEY("id"),
                FOREIGN KEY("propietario_id") REFERENCES "users"("id")
            );
        """))
        session.commit()