from flask import Flask, flash, jsonify, redirect, render_template, url_for, request, session
import secrets
import requests
from tempfile import mkdtemp
from flask_session import Session
from apps.ccoo_app.ccooQueries import *
from apps.ccoo_app.ccooApp import *
from flask import Blueprint
app = Flask(__name__)
ccooApp = Blueprint('ccooApp', __name__)


@ccooApp.route('/verNotas/CCOO/<int:codigo>', methods=["GET", "POST"])
def get_selected_content_ccoo(codigo):
    return get_content_ccoo(codigo)


@ccooApp.route('/nuevaSeccion/<int:codigo>', methods=["GET"])
def open_new_content_editor_ccoo(codigo):
    return render_template("ccoo_templates/nuevaSeccion.html", codigo=codigo)


@ccooApp.route('/upload', methods=["GET", "POST"])
def upload_content_ccoo():
    return upload_new_content_ccoo()


@ccooApp.route('/editar/<int:id>', methods=["GET", "POST"])
def edit_selected_content_ee(id):
    return edit_content_ccoo(id)
