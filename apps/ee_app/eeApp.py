from flask import Flask, flash, jsonify, redirect, render_template, url_for, request, session
import secrets
from tempfile import mkdtemp
from flask_session import Session
from flask import Blueprint, current_app
from apps.ee_app.eeQueries import *
app = Flask(__name__)
eeApp = Blueprint('eeApp', __name__)
__all__ = ["get_content_ee", "post_new_content_ee", "edit_content_ee"]


def get_content_ee(codigo):
    if codigo == 1240:
        session['nivelacion'] = 2
    if codigo == 1221:
        session['nivelacion'] = 1
    content = get_content_ee_query(codigo)
    return render_template("ee_templates/contenidoEE.html", content=content, codigo=codigo)


def post_new_content_ee():
    codigo = request.form.get('codigo')
    categoria = request.form.get('cmb')
    titulo = request.form.get('titulo')
    content = request.form.get('textArea')
    upload_content_ee_query(codigo, categoria, titulo, content)
    return redirect(url_for("eeApp.get_selected_content_ee", codigo=request.form.get("codigo")))


def edit_content_ee(id):
    if request.method == "GET":
        contentToEdit = get_content_to_edit_ee_query(id)
        return render_template("ee_templates/editarEE.html", contentToEdit=contentToEdit)
    elif request.method == "POST":
        codigo = request.form.get('codigo')
        categoria = request.form.get('cmb')
        titulo = request.form.get('titulo')
        content = request.form.get('textArea')
        edit_content_ee_query(codigo, categoria, titulo, content, id)
    return redirect(url_for("eeApp.get_selected_content_ee", codigo=request.form.get("codigo")))
