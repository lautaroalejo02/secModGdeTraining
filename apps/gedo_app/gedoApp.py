from flask import Flask, flash, jsonify, redirect, render_template, url_for, request, session
import secrets
from tempfile import mkdtemp
from flask_session import Session
from flask import Blueprint, current_app
from apps.gedo_app.gedoQueries import *
app = Flask(__name__)
gedoApp = Blueprint('gedoApp', __name__)
__all__ = ["get_content_gedo", "post_new_content_gedo", "edit_content_gedo"]


def get_content_gedo(codigo):
    def get_content_gedo(codigo):
    if codigo == 1321:
        session['nivelacion'] = 1
    if codigo == 1338:
        session['nivelacion'] = 2
    content = get_content_gedo_query(codigo)
    if codigo == 1337 and session['nivel'] == '2':
        level_up_gedo_query(session["user_id"])
    if codigo == 1369 and session['nivel'] == '6':
        level_up_gedo_query2(session["user_id"])
    return render_template("gedo_templates/contenidoGEDO.html", content=content, codigo=codigo)


def post_new_content_gedo():
    codigo = request.form.get('codigo')
    categoria = request.form.get('cmb')
    titulo = request.form.get('titulo')
    content = request.form.get('textArea')
    upload_content_gedo_query(codigo, categoria, titulo, content)
    return redirect(url_for('gedoApp.get_selected_content_gedo', codigo=codigo))


def edit_content_gedo(id):
    if request.method == "GET":
        contentToEdit = get_content_to_edit_gedo_query(id)
        return render_template("gedo_templates/editarGEDO.html", contentToEdit=contentToEdit)
    elif request.method == "POST":
        codigo = request.form.get('codigo')
        titulo = request.form.get('titulo')
        categoria = request.form.get('cmb')
        content = request.form.get('textArea')
        edit_content_gedo_query(codigo, titulo, categoria, content, id)
        return redirect(url_for("gedoApp.get_selected_content_gedo", codigo=request.form.get("codigo")))
