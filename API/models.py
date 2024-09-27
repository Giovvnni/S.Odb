from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Date
from sqlalchemy.orm import relationship
from API.database import Base

# Tabla Usuario
class Usuario(Base):
    __tablename__ = "usuario"
    usuario_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(20), nullable=False, unique=True)
    email = Column(String, nullable=False)
    contraseña = Column(String(16), nullable=False)
    fecha_registro = Column(Date, nullable=False)
    foto_perfil = Column(String, default="jpg", nullable=False)
    rol = Column(String, nullable=False)
    
    # Relación con Meme
    memes = relationship("Meme", back_populates="usuario")
    comentarios = relationship("Comentario", back_populates="usuario")
    votos = relationship("Voto", back_populates="usuario")


# Tabla Meme
class Meme(Base):
    __tablename__ = "meme"
    meme_id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuario.usuario_id"), nullable=False)
    fecha_subida = Column(Date, nullable=False)
    formato = Column(String, nullable=True)
    estado = Column(Boolean, nullable=False)

    usuario = relationship("Usuario", back_populates="memes")
    comentarios = relationship("Comentario", back_populates="meme")
    votos = relationship("Voto", back_populates="meme")
    etiquetas = relationship("Etiqueta", back_populates="meme")
    categorias = relationship("Categoria", back_populates="meme")



# Tabla Comentario
class Comentario(Base):
    __tablename__ = "comentario"
    comentario_id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuario.usuario_id"), nullable=False)
    meme_id = Column(Integer, ForeignKey("meme.meme_id"), nullable=False)
    fecha = Column(Date, nullable=True)
    contenido = Column(String, nullable=True)

    usuario = relationship("Usuario", back_populates="comentarios")
    meme = relationship("Meme", back_populates="comentarios")


# Tabla Etiqueta
class Etiqueta(Base):
    __tablename__ = "etiqueta"
    etiqueta_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=True)
    meme_id = Column(Integer, ForeignKey("meme.meme_id"), nullable=False)

    meme = relationship("Meme", back_populates="etiquetas")




# Tabla Categoria
class Categoria(Base):
    __tablename__ = "categoria"
    categoria_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False, default="Cualquiera")
    meme_id = Column(Integer, ForeignKey("meme.meme_id"), nullable=False)

    meme = relationship("Meme", back_populates="categorias")



# Tabla Voto
class Voto(Base):
    __tablename__ = "voto"
    voto_id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuario.usuario_id"), nullable=False)
    meme_id = Column(Integer, ForeignKey("meme.meme_id"), nullable=False)
    contador = Column(Integer, default=0, nullable=False)

    usuario = relationship("Usuario", back_populates="votos")
    meme = relationship("Meme", back_populates="votos")
