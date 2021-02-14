from cs50 import SQL
import sqlite3
from flask import Flask, flash, jsonify, redirect, render_template, url_for, request, session
import secrets
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from flask_session import Session
from apps.ccoo_app.ccooQueries import *
from flask import Blueprint
app = Flask(__name__)
ccooApp = Blueprint('ccooApp', __name__)

__all__ = ["get_content_ccoo", "upload_new_content_ccoo", "edit_content_ccoo"]


def get_content_ccoo(codigo):
    if codigo == 1158:
        session['nivelacion'] = 2
    if codigo == 1121:
        session['nivelacion'] = 1
    content = get_content_ccoo_query(codigo)
    if codigo == 1154 and session['nivel'] == '1':
        level_up_ccoo_query(session["user_id"])
    if codigo == 1171 and session['nivel'] == '4':
        level_up_ccoo_query2(session["user_id"])
    return render_template("ccoo_Templates/contenidoCCOO.html", content=content, codigo=codigo)


def upload_new_content_ccoo():
    formusername = request.form.get("textArea")
    codigo = request.form.get('codigo')
    categoria = request.form.get('cmb')
    titulo = request.form.get('titulo')
    content = request.form.get('textArea')
    upload_content_ccoo_query(codigo, categoria, titulo, content)

    return redirect(url_for("ccooApp.get_selected_content_ccoo", codigo=request.form.get("codigo")))


def edit_content_ccoo(id):
    if request.method == "GET":
        contentToEdit = content_editor_ccoo_query(id)
        return render_template("ccoo_templates/editar.html", contentToEdit=contentToEdit)

    elif request.method == "POST":
        codigo = request.form.get("codigo")
        titulo = request.form.get("titulo")
        categoria = request.form.get("cmb")
        contenido = request.form.get("textArea")
        edit_content_ccoo_query(id, codigo, titulo, categoria, contenido)
        return redirect(url_for("ccooApp.get_selected_content_ccoo", codigo=request.form.get("codigo")))
