# main.py
from fastapi import FastAPI
from API.routes import router
from API import models
from API.database import engine

# Crear las tablas de la base de datos
models.Base.metadata.create_all(bind=engine)

# Crear la instancia de la aplicación FastAPI
app = FastAPI()

# Incluir el router que definimos en crud.py
app.include_router(router)
