from cs50 import SQL
import sqlite3
import secrets
from flask_session import Session
from database_init import db


def register_query(cuil, username,  password, reparticion, email, nombre, apellido, rol, nivel):
    print("hola")
    db.execute("INSERT INTO users(usu_Cuil,usu_Username,usu_Password,usu_Reparticion,usu_Email,usu_Nombre,usu_Apellido,usu_Rol,usu_Nivel) VALUES (:cuil,:username,:password,:reparticion,:email,:nombre,:apellido,:rol,:nivel)",
               cuil=cuil,
               username=username,
               password=password,
               reparticion=reparticion,
               email=email,
               nombre=nombre,
               apellido=apellido,
               rol=rol,
               nivel=nivel
               )
    return None


def login_query(username):
    user = db.execute("SELECT * FROM users WHERE usu_username = :username",
                      username=username)
    return user


def check_username():
    users = db.execute("SELECT usu_Username FROM users")
    return users


def get_all_users_query():
    all_users = db.execute("""
    SELECT usu_Id,usu_Cuil,usu_Username,usu_Nombre,usu_Apellido,usu_Email,usu_Rol,usu_Reparticion,usu_Nivel
    FROM users
    """)
    return all_users


def get_user_by_user_by_id_query(id):
    user = db.execute("""
    SELECT usu_Id,usu_Cuil,usu_Username,usu_Nombre,usu_Apellido,usu_Email,usu_Rol,usu_Reparticion,usu_Nivel
    FROM users
    WHERE usu_id = :user_Id
    """, user_Id=id)
    return user


def modify_user_query(user_Id, cuil, username,  passwordHash, reparticion, email, nombre, apellido, nivel):
    db.execute("""
            UPDATE users SET usu_Cuil=:cuil,usu_Username=:username,usu_Nombre=:nombre,usu_Apellido=:apellido,usu_Email=:email,usu_Reparticion=:reparticion, usu_Password=:password,usu_Nivel=:nivel WHERE usu_Id = :user_Id
            """,
               user_Id=user_Id,
               cuil=cuil,
               username=username,
               nombre=nombre,
               apellido=apellido,
               email=email,
               reparticion=reparticion,
               password=passwordHash,
               nivel=nivel)
    return None


def delete_user_query(id):
    db.execute("""
    DELETE FROM users Where usu_Id = :user_Id
    """,
               user_Id=id
               )
    return None


def save_user_survey_query(contenido, usu_id, seccion):
    db.execute("INSERT INTO encuesta(enc_Contenido,usu_Id,enc_Seccion) VALUES (:contenido,:usu_Id,:seccion)",
               contenido=contenido,
               usu_Id=usu_id,
               seccion=seccion)


def get_all_surveys_query():
    surveys = db.execute("""
    SELECT enc_Id, enc_Contenido,enc_Seccion, enc_Fecha, usu_Nombre, usu_Apellido,usu_Cuil,usu_Reparticion
    FROM encuesta
    LEFT JOIN
    users ON users.usu_Id = encuesta.usu_Id
    """)
    return surveys


def delete_survey_query(id):
    db.execute("""
    DELETE FROM encuesta Where enc_Id = :enc_Id
    """,
               enc_Id=id
               )
