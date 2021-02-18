from cs50 import SQL
import sqlite3
import requests
import sys
from flask import Flask, flash, jsonify, redirect, render_template, url_for, session, request
import secrets
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from flask_session import Session
from flask_mail import Mail, Message
from helper import error, exito
from apps.ccoo_app.ccooApp import *
from apps.ccoo_app.ccooRoutes import *
from apps.ee_app.eeApp import *
from apps.ee_app.eeRoutes import *
from apps.gedo_app.gedoApp import *
from apps.gedo_app.gedoRoutes import *
from apps.users_app.usersApp import *
from apps.users_app.users_Routes import *
from helper import *
from database_init import db
app = Flask(__name__)
app.register_blueprint(ccooApp)
app.register_blueprint(eeApp)
app.register_blueprint(gedoApp)
app.register_blueprint(usersApp)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/')
def index():
    return render_template("inicio.html")


@app.route('/cursos')
def cursos():
    if session.get('logged_in') == True:
        rows = db.execute(
            "SELECT * FROM users WHERE usu_Id = :Id", Id=session["user_id"])
        session['rol'] = rows[0]["usu_Rol"]
        session['email'] = rows[0]["usu_Email"]
        session['nivel'] = rows[0]["usu_Nivel"]
        print(session['nivel'])
    return render_template("cursos.html")


@app.route("/contacto")
def contacto():
    return render_template("contacto.html")


@app.route("/sendMail", methods=["POST"])
def sendMail():
    try:
        body = "This is message from" + request.form.get("email") + "\r\n"
        html = """<html>
            <h5>Mail del usuario que realizo la consulta:</h5> """ + request.form.get("email")+"""
            </html>
            """ + request.form.get("textArea")
        subject = request.form.get("asunto")
        recipient = 'capacitaciongde@jujuy.gob.ar'
        send_email(body, html, subject, recipient)
        return exito("Su mensaje fue enviado con exito")
    except:
        return error("Revise los campos e intente nuevamente")


@app.route("/dudas")
def dudas():
    return render_template("dudasyConsultas.html")


@app.route("/sendConsulta", methods=["POST"])
def sendConsulta():
    try:
        body = "Este mensaje fue enviado por: " + session['email'] + "\r\n"
        html = """<html>
            <h5>Duda o Consulta:</h5> """ + session['email']+"""
            </html>
            """ + request.form.get("textArea")
        subject = request.form.get("asunto")
        recipient = 'capacitaciongde@jujuy.gob.ar'
        send_email(body, html, subject, recipient)
        return exito("Su mensaje fue enviado con exito")
    except:
        return error("Revise los campos e intente nuevamente")


if __name__ == "__main__":
    app.run(debug=True)
