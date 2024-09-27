# crud.py
from sqlalchemy import text
from datetime import date
from sqlalchemy.orm import Session
from API.models import Usuario, Meme, Comentario, Etiqueta, Categoria, Voto
from sqlalchemy import update

# INSERT
def crear_usuario(db: Session, nombre: str, email: str, contraseña: str, fecha_registro, rol: str):
    nuevo_usuario = Usuario(nombre=nombre, email=email, contraseña=contraseña, fecha_registro=fecha_registro, rol=rol)
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

def crear_meme(db: Session, usuario_id: int, fecha_subida, formato: str, estado: bool):
    nuevo_meme = Meme(usuario_id=usuario_id, fecha_subida=fecha_subida, formato=formato, estado=estado)
    db.add(nuevo_meme)
    db.commit()
    db.refresh(nuevo_meme)
    return nuevo_meme

def crear_comentario(db: Session, usuario_id: int, meme_id: int, contenido: str):
    nuevo_comentario = Comentario(usuario_id=usuario_id, meme_id=meme_id, fecha=date.today(), contenido=contenido)
    db.add(nuevo_comentario)
    db.commit()
    db.refresh(nuevo_comentario)
    return nuevo_comentario

# SELECT
def obtener_todos_los_usuarios(db: Session):
    return db.query(Usuario).all()

def obtener_todos_los_memes(db: Session):
    return db.query(Meme).all()

def obtener_todos_los_comentarios(db: Session):
    return db.query(Comentario).all()

# SELECT (con JOIN)

def obtener_memes_usuario(db: Session):
    resultados = db.query(Meme, Usuario).join(Usuario).all()
    # Convertir los resultados a una lista de diccionarios, si no, ocurría un error.
    return [
        {
            "meme_id": meme.meme_id,
            "usuario_id": usuario.usuario_id,
            "fecha_subida": meme.fecha_subida,
            "formato": meme.formato,
            "estado": meme.estado,
            "usuario_nombre": usuario.nombre,
        }
        for meme, usuario in resultados
    ]

def obtener_comentarios_usuario(db: Session):
    resultados = (
        db.query(Comentario, Meme, Usuario)
        .join(Meme, Comentario.meme_id == Meme.meme_id)
        .join(Usuario, Comentario.usuario_id == Usuario.usuario_id)
        .all()
    )
    
    # Convertir los resultados a una lista de diccionarios, si no, ocurría un error.
    comentarios_dicc = []
    for comentario, meme, usuario in resultados:
        comentarios_dicc.append({
            "comentario_id": comentario.comentario_id,
            "contenido": comentario.contenido,
            "fecha": comentario.fecha,
            "meme_id": meme.meme_id,
            "usuario_id": usuario.usuario_id,
            "nombre": usuario.nombre,
                
        })

    return comentarios_dicc

# UPDATE
def actualizar_nombre_usuario(db: Session, usuario_id: int, nuevo_nombre: str):
    db.query(Usuario).filter(Usuario.usuario_id == usuario_id).update({Usuario.nombre: nuevo_nombre})
    db.commit()

def actualizar_estado_meme(db: Session, meme_id: int, nuevo_estado: bool):
    db.query(Meme).filter(Meme.meme_id == meme_id).update({Meme.estado: nuevo_estado})
    db.commit()

# DELETE
def borrar_usuario(db: Session, usuario_id: int):
    usuario = db.query(Usuario).filter(Usuario.usuario_id == usuario_id).first()
    if usuario:
        db.delete(usuario)
        db.commit()

def borrar_meme(db: Session, meme_id: int):
    meme = db.query(Meme).filter(Meme.meme_id == meme_id).first()
    if meme:
        db.delete(meme)
        db.commit()
        

# ALTER
def agregar_descripcion(db: Session):
    db.execute(text("ALTER TABLE meme ADD COLUMN descripcion VARCHAR(255)"))
    db.commit()

def modificar_largo_contraseña(db: Session):
    db.execute(text("ALTER TABLE usuario MODIFY COLUMN contraseña VARCHAR(20)"))
    db.commit()

# DROP
def borrar_tabla_voto(db: Session):
    db.execute(text("DROP TABLE IF EXISTS voto"))
    db.commit()

def borrar_columna_descripcion(db: Session):
    db.execute(text("ALTER TABLE meme DROP COLUMN descripcion"))
    db.commit()
