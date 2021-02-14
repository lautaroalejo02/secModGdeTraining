from cs50 import SQL
import sqlite3
import secrets
from flask_session import Session
from apps.ccoo_app.ccooQueries import *
from database_init import db
__all__ = ["get_content_ccoo_query", "level_up_ccoo_query",
           "upload_content_ccoo_query", "content_editor_ccoo_query", "edit_content_ccoo_query", "level_up_ccoo_query2"]


def get_content_ccoo_query(codigo):
    content = db.execute("""
    SELECT co_Id,co_Titulo,co_Contenido
    FROM courses
    WHERE
    co_Codigo = :co_Codigo
    """, co_Codigo=codigo)
    return content


def level_up_ccoo_query(id):
    db.execute("""UPDATE users SET usu_Nivel=:usu_Nivel
        WHERE usu_Id = :Id
        """,
               usu_Nivel=2,
               Id=id)
    return None


def level_up_ccoo_query2(id):
    db.execute("""UPDATE users SET usu_Nivel=:usu_Nivel
        WHERE usu_Id = :Id
        """,
               usu_Nivel='5',
               Id=id)
    return None


def upload_content_ccoo_query(codigo, categoria, titulo, content):
    db.execute("INSERT INTO courses(co_Codigo,co_Categoria,co_Titulo,co_Contenido) VALUES (:codigo,:categoria,:titulo,:content)",
               codigo=codigo,
               categoria=categoria,
               titulo=titulo,
               content=content,
               )


def content_editor_ccoo_query(id):
    contentToEdit = db.execute("""
        SELECT co_Id,co_Codigo,co_Categoria,co_Titulo,co_Contenido
        FROM courses
        WHERE
        co_Id = :co_Id
        """, co_Id=id)
    return contentToEdit


def edit_content_ccoo_query(id, codigo, titulo, categoria, contenido):
    db.execute("""
            UPDATE courses SET co_Codigo=:codigo,co_Titulo=:titulo,co_Categoria=:categoria,co_Contenido=:contenido WHERE co_Id = :Id

            """,
               codigo=codigo,
               titulo=titulo,
               categoria=categoria,
               contenido=contenido,
               Id=id)
    return codigo
