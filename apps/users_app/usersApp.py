from flask import Flask, flash, jsonify, redirect, render_template, url_for, request, session
import secrets
from tempfile import mkdtemp
from flask_session import Session
from flask import Blueprint, current_app
from apps.users_app.usersQueries import *
from helper import error, exito, send_email
from werkzeug.security import check_password_hash, generate_password_hash
app = Flask(__name__)
usersApp = Blueprint('usersApp', __name__)
__all__ = ["register_user", "login", "logout",
           "get_all_users",  "modify_user", "get_user_by_id", "delete_user", "survey", "all_surveys", "delete_survey"]


def register_user():
    if request.method == "GET":
        return render_template("authentication/register.html")
    elif request.method == "POST":
        nivel = 1
        if not request.form.get('cuil'):
            return error("Revise el cuil e intente nuevamente")
        if not request.form.get('username'):
            return error("Revise el username e intente nuevamente")
        if not request.form.get('reparticion'):
            return error("Revise la reparticion e intente nuevamente")
        if not request.form.get('email'):
            return error("Revise el email e intente nuevamente")
        if not request.form.get('nombre'):
            return error("Revise el nombre e intente nuevamente")
        if not request.form.get('apellido'):
            return error("Revise el apellido e intente nuevamente")
        usernames = check_username()
        if not request.form.get('username' in usernames):
            return error("Username en uso, elija otro e intente nuevamente")
        try:
            if session["rol"] != 3:
                rol = 1
            else:
                rol = request.form.get('rol')
            cuil = request.form.get('cuil'),
            username = request.form.get('username'),
            password = generate_password_hash(request.form.get('password')),
            reparticion = request.form.get('reparticion'),
            email = request.form.get('email'),
            nombre = request.form.get('nombre'),
            apellido = request.form.get('apellido'),
            rol = rol,
            nivel = nivel
            register_query(cuil, username, password, reparticion,
                           email, nombre, apellido, rol, nivel)
            body = "This is message from" + request.form.get("email") + "\r\n"
            html = """<html>
            <p style='margin: 0px 0px 8px; text-overflow: ellipsis; overflow-wrap: break-word; color: rgb(23, 43, 77); font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans", Ubuntu, "Droid Sans", "Helvetica Neue", sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;'>Desde la Secretar&iacute;a de Modernizaci&oacute;n comunicamos que fue habilitado para la capacitaci&oacute;n en la Plataforma GDE Training.</p>
            <p style='margin: 0px 0px 8px; text-overflow: ellipsis; overflow-wrap: break-word; color: rgb(23, 43, 77); font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans", Ubuntu, "Droid Sans", "Helvetica Neue", sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;'>Para ingreso&nbsp;<a href="https://www.gdetraining.com/" rel="noreferrer nofollow" style="background-color: transparent; color: rgb(23, 43, 77);" target="_blank">https://www.gdetraining.com/</a><br>Usuario:""" + request.form.get('username')+"""<br>Clave:""" + request.form.get('password')+"""</p>
            <p style='margin: 0px 0px 8px; text-overflow: ellipsis; overflow-wrap: break-word; color: rgb(23, 43, 77); font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans", Ubuntu, "Droid Sans", "Helvetica Neue", sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;'>La capacitaci&oacute;n finaliza el 25 de febrero del corriente a&ntilde;o, espacio en el cu&aacute;l deber&aacute; completar todas las actividades requeridas.</p>
            <p style='margin: 0px; text-overflow: ellipsis; overflow-wrap: break-word; color: rgb(23, 43, 77); font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans", Ubuntu, "Droid Sans", "Helvetica Neue", sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;'>Canales de comunicaci&oacute;n para acceder a tutores<br>What app 388 4383563 7-13h d&iacute;as laborables<br>Mail&nbsp;<a href="mailto:capacitaciongde@jujuy.gob.ar" style="background-color: transparent; color: rgb(23, 43, 77);">capacitaciongde@jujuy.gob.ar</a></p>
            </html>"""
            subject = 'Confirmacion de registro Secretaria de modernizacion'
            recipient = request.form.get("email")
            try:
                send_email(body, html, subject, recipient)
            except:
                error(
                    "Hubo un error al enviar el mail. Enviarlo manualmente o revisar el mail")
            return redirect(url_for("cursos"))
        except:
            return error("Revise los campos e intente nuevamente")


def login():
    username = request.form.get("username")
    if request.method == "POST":
        user = login_query(username)
        if len(user) != 1 or not check_password_hash(user[0]["usu_Password"], request.form.get("password")):
            return error("Revise los campos e intente nuevamente")
        session["user_id"] = user[0]["usu_Id"]
        session['logged_in'] = True
        session['rol'] = user[0]["usu_Rol"]
        session['email'] = user[0]["usu_Email"]
        session['nivel'] = user[0]["usu_Nivel"]
        return redirect("/")
    elif request.method == "GET":
        return render_template("authentication/login.html")


def logout():
    session['logged_in'] = False
    session.clear()
    return redirect(url_for("cursos"))


def get_all_users():
    userss = get_all_users_query()
    return render_template("users_control_templates/adminUsers.html", userss=userss)


def get_user_by_id(id):
    userSelected = get_user_by_user_by_id_query(id)
    session['nivel2'] = userSelected[0]["usu_Nivel"]
    return render_template("users_control_templates/modificarUser.html", userSelected=userSelected)


def modify_user():
    password = request.form.get("password")
    passwordHash = generate_password_hash(password)
    if session['nivel2'] != '4':
        if request.form.get("nivel") == '4':
            mail_body = "This is message from"
            mail_html = """<html>
            <p style='margin: 0px 0px 8px; text-overflow: ellipsis; overflow-wrap: break-word; color: rgb(23, 43, 77); font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans", Ubuntu, "Droid Sans", "Helvetica Neue", sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;'>Desde la Secretar&iacute;a de Modernizaci&oacute;n comunicamos que fue habilitado para el segundo nivel de la capacitaci&oacute;n en la Plataforma GDE Training.</p>
            <p style='margin: 0px 0px 8px; text-overflow: ellipsis; overflow-wrap: break-word; color: rgb(23, 43, 77); font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans", Ubuntu, "Droid Sans", "Helvetica Neue", sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;'>Para ingresar al segundo nivel de la capacitacion ingrese a la plataforma <a href="www.gdetraining.com">https://www.gdetraining.com</a> con sus credenciales</p>
            <p style='margin: 0px; text-overflow: ellipsis; overflow-wrap: break-word; color: rgb(23, 43, 77); font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans", Ubuntu, "Droid Sans", "Helvetica Neue", sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;'>Canales de comunicaci&oacute;n para acceder a tutores<br>What app 388 4383563 7-13h d&iacute;as laborables<br>Mail&nbsp;<a href="mailto:capacitaciongde@jujuy.gob.ar" style="background-color: transparent; color: rgb(23, 43, 77);">capacitaciongde@jujuy.gob.ar</a></p>
            </html>"""
            mail_subject = "Segundo nivel GDE Training"
            mail_recipient = request.form.get("email")
            send_email(mail_body, mail_html, mail_subject, mail_recipient)
    user_Id = request.form.get('id')
    cuil = request.form.get('cuil')
    username = request.form.get('username')
    password = passwordHash
    reparticion = request.form.get('reparticion')
    email = request.form.get('email')
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    nivel = request.form.get("nivel")
    modify_user_query(user_Id, cuil, username,  password, reparticion,
                      email, nombre, apellido, nivel)
    return redirect(url_for("usersApp.all_users"))


def delete_user(id):
    delete_user_query(id)
    return redirect(url_for("usersApp.all_users"))


def survey():
    if request.method == "GET":
        return render_template("users_control_templates/encuesta.html")
    elif request.method == "POST":
        contenido = request.form.get("contenido"),
        usu_id = session["user_id"],
        seccion = request.form.get("cmb"),
        save_user_survey_query(contenido, usu_id, seccion)
        return redirect(url_for("cursos"))


def all_surveys():
    if request.method == "GET":
        encuestas = get_all_surveys_query()
    return render_template("users_control_templates/verEncuesta.html", encuestas=encuestas)


def delete_survey(id):
    delete_survey_query(id)
    return redirect(url_for("usersApp.user_survey"))
