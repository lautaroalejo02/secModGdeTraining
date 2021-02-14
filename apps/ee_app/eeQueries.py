from cs50 import SQL
import sqlite3
import secrets
from flask_session import Session
from database_init import db


def get_content_ee_query(codigo):
    content = db.execute("""
    SELECT co_Id,co_Codigo,co_Titulo,co_Contenido
    FROM courseee
    WHERE
    co_Codigo = :co_Codigo
    """, co_Codigo=codigo)
    return content


def upload_content_ee_query(codigo, categoria, titulo, content):
    db.execute("INSERT INTO courseee(co_Codigo,co_Categoria,co_Titulo,co_Contenido) VALUES (:codigo,:categoria,:titulo,:content)",
               codigo=codigo,
               categoria=categoria,
               titulo=titulo,
               content=content,
               )


def get_content_to_edit_ee_query(id):
    contentToEdit = db.execute("""
        SELECT co_Id,co_Codigo,co_Categoria,co_Titulo,co_Contenido
        FROM courseee
        WHERE
        co_Id = :co_Id
        """, co_Id=id)
    return contentToEdit


def edit_content_ee_query(codigo, categoria, titulo, content, id):
    db.execute("""
            UPDATE courseee SET co_Codigo=:codigo,co_Titulo=:titulo,co_Categoria=:categoria,co_Contenido=:content WHERE co_Id = :Id
            """,
               codigo=codigo,
               categoria=categoria,
               titulo=titulo,
               content=content,
               Id=id)
