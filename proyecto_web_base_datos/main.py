from fastapi import FastAPI, Request, Form, HTTPException, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import ValidationError
from typing import Optional, Annotated
from sqlalchemy.orm import Session
import crud
import schemas
from models import crear_tablas
from database import get_db

# Crear las tablas en la base de datos al iniciar la aplicación
crear_tablas()

app = FastAPI(
    title="Aplicación Web CRUD con FastAPI",
    version="1.0.0", 
    description="Una aplicación web completa con operaciones CRUD usando FastAPI, SQLAlchemy y Jinja2"
)

# Configurar archivos estáticos y plantillas
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# Función auxiliar para manejar mensajes
def get_messages(request: Request):
    messages = request.session.get('messages', [])
    if messages:
        request.session['messages'] = []
    return messages

# Ruta principal
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html", 
        {"request": request}
    )

# Rutas de usuarios
@app.get("/users", response_class=HTMLResponse)
async def list_users(request: Request, db: Annotated[Session, Depends(get_db)]):
    users = crud.get_users(db)
    return templates.TemplateResponse(
        "users.html", 
        {"request": request, "users": users}
    )

@app.get("/users/create", response_class=HTMLResponse)
async def create_user_form(request: Request):
    return templates.TemplateResponse(
        "user_form.html", 
        {"request": request}
    )

@app.post("/users/create")
async def create_user(
    request: Request,
    db: Annotated[Session, Depends(get_db)],
    email: str = Form(...),
    password: str = Form(...)
):
    try:
        # Validar datos usando Pydantic
        user_data = schemas.UserCreate(email=email, password=password)
        
        # Verificar si el email ya existe
        existing_user = crud.get_user_by_email(db, email=user_data.email)
        if existing_user:
            return templates.TemplateResponse(
                "user_form.html",
                {
                    "request": request,
                    "errors": ["El email ya está registrado"],
                    "form_data": {"email": email}
                }
            )
        
        # Crear el usuario
        crud.create_user(db=db, user=user_data)
        return RedirectResponse(url="/users", status_code=303)
        
    except ValidationError as e:
        errors = [error['msg'] for error in e.errors()]
        return templates.TemplateResponse(
            "user_form.html",
            {
                "request": request,
                "errors": errors,
                "form_data": {"email": email}
            }
        )
    except Exception as e:
        return templates.TemplateResponse(
            "user_form.html",
            {
                "request": request,
                "errors": [f"Error al crear usuario: {str(e)}"],
                "form_data": {"email": email}
            }
        )

@app.get("/users/{user_id}", response_class=HTMLResponse)
async def user_detail(request: Request, user_id: int, db: Annotated[Session, Depends(get_db)]):
    user = crud.get_user(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    items = crud.get_items_by_user(db, user_id=user_id)
    return templates.TemplateResponse(
        "user_detail.html",
        {"request": request, "user": user, "items": items}
    )

@app.get("/users/{user_id}/edit", response_class=HTMLResponse)
async def edit_user_form(request: Request, user_id: int, db: Annotated[Session, Depends(get_db)]):
    user = crud.get_user(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    return templates.TemplateResponse(
        "user_form.html",
        {"request": request, "user": user}
    )

@app.post("/users/{user_id}/edit")
async def edit_user(
    request: Request,
    user_id: int,
    db: Annotated[Session, Depends(get_db)],
    email: str = Form(...)
):
    try:
        user = crud.get_user(db, user_id=user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        # Verificar si el email ya existe en otro usuario
        existing_user = crud.get_user_by_email(db, email=email)
        if existing_user and existing_user['id'] != user_id:
            return templates.TemplateResponse(
                "user_form.html",
                {
                    "request": request,
                    "user": user,
                    "errors": ["El email ya está registrado por otro usuario"]
                }
            )
        
        # Actualizar el usuario
        crud.update_user(db=db, user_id=user_id, new_email=email)
        return RedirectResponse(url=f"/users/{user_id}", status_code=303)
        
    except Exception as e:
        return templates.TemplateResponse(
            "user_form.html",
            {
                "request": request,
                "user": user,
                "errors": [f"Error al actualizar usuario: {str(e)}"]
            }
        )

# Rutas de items
@app.get("/items", response_class=HTMLResponse)
async def list_items(request: Request, db: Annotated[Session, Depends(get_db)]):
    items = crud.get_items(db)
    return templates.TemplateResponse(
        "items.html",
        {"request": request, "items": items}
    )

@app.get("/items/create", response_class=HTMLResponse)
async def create_item_form(request: Request, db: Annotated[Session, Depends(get_db)]):
    users = crud.get_users(db)
    return templates.TemplateResponse(
        "item_form.html",
        {"request": request, "users": users}
    )

@app.post("/items/create")
async def create_item(
    request: Request,
    db: Annotated[Session, Depends(get_db)],
    nombre: str = Form(...),
    descripcion: Optional[str] = Form(None),
    propietario_id: int = Form(...)
):
    try:
        # Validar que el usuario existe
        user = crud.get_user(db, user_id=propietario_id)
        if not user:
            users = crud.get_users(db)
            return templates.TemplateResponse(
                "item_form.html",
                {
                    "request": request,
                    "users": users,
                    "errors": ["El usuario seleccionado no existe"],
                    "form_data": {"nombre": nombre, "descripcion": descripcion, "propietario_id": propietario_id}
                }
            )
        
        # Crear el item
        item_data = schemas.ItemCreate(nombre=nombre, descripcion=descripcion)
        crud.create_user_item(db=db, item=item_data, user_id=propietario_id)
        return RedirectResponse(url="/items", status_code=303)
        
    except ValidationError as e:
        users = crud.get_users(db)
        errors = [error['msg'] for error in e.errors()]
        return templates.TemplateResponse(
            "item_form.html",
            {
                "request": request,
                "users": users,
                "errors": errors,
                "form_data": {"nombre": nombre, "descripcion": descripcion, "propietario_id": propietario_id}
            }
        )
    except Exception as e:
        users = crud.get_users(db)
        return templates.TemplateResponse(
            "item_form.html",
            {
                "request": request,
                "users": users,
                "errors": [f"Error al crear item: {str(e)}"],
                "form_data": {"nombre": nombre, "descripcion": descripcion, "propietario_id": propietario_id}
            }
        )

@app.get("/users/{user_id}/items/create", response_class=HTMLResponse)
async def create_user_item_form(request: Request, user_id: int, db: Annotated[Session, Depends(get_db)]):
    user = crud.get_user(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    return templates.TemplateResponse(
        "item_form.html",
        {"request": request, "user_id": user_id, "user_email": user['email']}
    )

@app.post("/users/{user_id}/items/create")
async def create_user_item(
    request: Request,
    user_id: int,
    db: Annotated[Session, Depends(get_db)],
    nombre: str = Form(...),
    descripcion: Optional[str] = Form(None),
    propietario_id: int = Form(...)
):
    try:
        # Verificar que los IDs coinciden
        if user_id != propietario_id:
            raise HTTPException(status_code=400, detail="ID de usuario no coincide")
        
        # Validar que el usuario existe
        user = crud.get_user(db, user_id=user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        # Crear el item
        item_data = schemas.ItemCreate(nombre=nombre, descripcion=descripcion)
        crud.create_user_item(db=db, item=item_data, user_id=user_id)
        return RedirectResponse(url=f"/users/{user_id}", status_code=303)
        
    except ValidationError as e:
        errors = [error['msg'] for error in e.errors()]
        return templates.TemplateResponse(
            "item_form.html",
            {
                "request": request,
                "user_id": user_id,
                "user_email": user['email'],
                "errors": errors,
                "form_data": {"nombre": nombre, "descripcion": descripcion}
            }
        )
    except Exception as e:
        return templates.TemplateResponse(
            "item_form.html",
            {
                "request": request,
                "user_id": user_id,
                "user_email": user['email'] if 'user' in locals() else None,
                "errors": [f"Error al crear item: {str(e)}"],
                "form_data": {"nombre": nombre, "descripcion": descripcion}
            }
        )

@app.get("/items/{item_id}/edit", response_class=HTMLResponse)
async def edit_item_form(request: Request, item_id: int, db: Annotated[Session, Depends(get_db)]):
    item = crud.get_item(db, item_id=item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    
    return templates.TemplateResponse(
        "item_form.html",
        {"request": request, "item": item}
    )

@app.post("/items/{item_id}/edit")
async def edit_item(
    request: Request,
    item_id: int,
    db: Annotated[Session, Depends(get_db)],
    nombre: str = Form(...),
    descripcion: Optional[str] = Form(None)
):
    try:
        item = crud.get_item(db, item_id=item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Item no encontrado")
        
        # Actualizar el item
        item_data = schemas.ItemCreate(nombre=nombre, descripcion=descripcion)
        crud.update_item(db=db, item_id=item_id, item=item_data)
        return RedirectResponse(url="/items", status_code=303)
        
    except ValidationError as e:
        errors = [error['msg'] for error in e.errors()]
        return templates.TemplateResponse(
            "item_form.html",
            {
                "request": request,
                "item": item,
                "errors": errors
            }
        )
    except Exception as e:
        return templates.TemplateResponse(
            "item_form.html",
            {
                "request": request,
                "item": item,
                "errors": [f"Error al actualizar item: {str(e)}"]
            }
        )

@app.post("/items/{item_id}/delete")
async def delete_item(item_id: int, db: Annotated[Session, Depends(get_db)]):
    try:
        crud.delete_item(db=db, item_id=item_id)
        return RedirectResponse(url="/items", status_code=303)
    except HTTPException:
        return RedirectResponse(url="/items", status_code=303)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)