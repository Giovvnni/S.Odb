from pydantic import BaseModel
from datetime import date


class UsuarioCreate(BaseModel):
    nombre: str
    email: str
    contraseña: str
    fecha_registro: date
    foto_perfil: str = "imagen por defecto"
    rol: str


class UsuarioResponse(BaseModel):
    usuario_id: int
    nombre: str
    email: str
    fecha_registro: date
    foto_perfil: str
    rol: str

    class Config:
        orm_mode = True  
