
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from API import crud  # importar funciones de CRUD
from API.database import get_db  # la función get_db para obtener la base de datos

# Crear un router para definir las rutas
router = APIRouter()

# Insertar un usuario
@router.post("/insert/usuarios_insert/")
def crear_usuario(nombre: str, email: str, contraseña: str, fecha_registro, rol: str, db: Session = Depends(get_db)):
    return crud.crear_usuario(db, nombre, email, contraseña, fecha_registro, rol)

## Insertar un meme
@router.post("/insert/memes_insert/")
def crear_meme(usuario_id: int, fecha_subida, formato: str, estado: bool, db: Session = Depends(get_db)):
    return crud.crear_meme(db, usuario_id, fecha_subida, formato, estado)

# Insertar un comentario 
@router.post("/insert/comentarios_insert/")
def crear_comentario(usuario_id: int, meme_id: int, contenido: str, db: Session = Depends(get_db)):
    return crud.crear_comentario(db, usuario_id, meme_id, contenido)
# Listar todos los usuarios
@router.get("/select/usuarios_select/")
def listar_usuarios(db: Session = Depends(get_db)):
    return crud.obtener_todos_los_usuarios(db)

# Listar todos los memes
@router.get("/select/memesselect/")
def listar_memes(db: Session = Depends(get_db)):
    return crud.obtener_todos_los_memes(db)

# Listar todos los comentarios
@router.get("/select/comentarios_select/")
def listar_comentarios(db: Session = Depends(get_db)):
    return crud.obtener_todos_los_comentarios(db)

# Obtener detalles memes con detalle del usuario que los subió
@router.get("/select_join/memes_user_join/")
def obtener_memes_con_usuario(db: Session = Depends(get_db)):
    return crud.obtener_memes_usuario(db)

# Obtener comentarios de meme y el usuario
@router.get("/select_join/comentarios_join/")
def obtener_comentarios_con_meme_usuario(db: Session = Depends(get_db)):
    return crud.obtener_comentarios_usuario(db)

# Actualizar nombre de usuario
@router.put("/update/usuarios_update/{usuario_id}")
def actualizar_nombre_usuario(usuario_id: int, nuevo_nombre: str, db: Session = Depends(get_db)):
    crud.actualizar_nombre_usuario(db, usuario_id, nuevo_nombre)
    return {"mensaje": "Usuario actualizado"}

# Actualizar estado de un meme
@router.put("/update/memes_update/{meme_id}")
def actualizar_estado_meme(meme_id: int, nuevo_estado: bool, db: Session = Depends(get_db)):
    crud.actualizar_estado_meme(db, meme_id, nuevo_estado)
    return {"mensaje": "Meme actualizado"}

# Eliminar un usuario
@router.delete("/delete/usuarios_delete/{usuario_id}")
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    crud.borrar_usuario(db, usuario_id)
    return {"mensaje": "Usuario eliminado"}

# Eliminar meme
@router.delete("/delete/meme_delete/")
def eliminar_meme(meme_id: int, db: Session = Depends(get_db)):
    crud.borrar_meme(db, meme_id)
    return {"mensaje": "Meme eliminado correctamente"}

# Alterar la tabla meme para agregar una columna de descripción en tabla meme
@router.post("/alter/meme_alter/")
def agregar_columna_descripcion(db: Session = Depends(get_db)):
    crud.agregar_descripcion(db)
    return {"mensaje": "Columna descripción agregada"}

# Alterar la tabla usuario para modificar el largo de la contraseña
@router.post("/alter/usuario_contraseña")
def modificar_largo_contraseña(db: Session = Depends(get_db)):
    crud.modificar_largo_contraseña(db)
    return {"mensaje": "Largo contraseña actualizado"}

# drop la tabla de votos 
@router.delete("/drop/voto_drop")
def eliminar_tabla_voto(db: Session = Depends(get_db)):
    crud.borrar_tabla_voto(db)
    return {"mensaje": "Tabla voto eliminada"}

#drop columna descripcion
@router.delete("/drop/descripcion_drop")
def eliminar_columna_descripcion(db: Session = Depends(get_db)):
    crud.borrar_columna_descripcion(db)
    return {"mensaje": "Tabla descripcion eliminada"}

    
