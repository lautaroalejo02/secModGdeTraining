from cs50 import SQL
import sqlite3
from database_init import db


def get_content_gedo_query(codigo):
    content = db.execute("""
    SELECT co_Id,co_Codigo,co_Titulo,co_Contenido
    FROM coursegedo
    WHERE
    co_Codigo = :co_Codigo
    """, co_Codigo=codigo)
    return content


def level_up_gedo_query(id):
    db.execute("""UPDATE users SET usu_Nivel=:usu_Nivel
        WHERE usu_Id = :Id
        """,
               usu_Nivel='3',
               Id=id)


def upload_content_gedo_query(codigo, categoria, titulo, content):
    db.execute("INSERT INTO coursegedo(co_Codigo,co_Categoria,co_Titulo,co_Contenido) VALUES (:codigo,:categoria,:titulo,:content)",
               codigo=codigo,
               categoria=categoria,
               titulo=titulo,
               content=content,
               )


def get_content_to_edit_gedo_query(id):
    contentToEdit = db.execute("""
    SELECT co_Id,co_Codigo,co_Categoria,co_Titulo,co_Contenido
    FROM coursegedo
    WHERE
    co_Id = :co_Id
    """, co_Id=id)
    return contentToEdit


def edit_content_gedo_query(codigo, titulo, categoria,  content, id):
    db.execute("""
            UPDATE coursegedo SET co_Codigo=:codigo,co_Titulo=:titulo,co_Categoria=:categoria,co_Contenido=:contenido WHERE co_Id = :Id
            """,
               codigo=codigo,
               titulo=titulo,
               categoria=categoria,
               contenido=content,
               Id=id)
