from flask import Flask, flash, jsonify, redirect, render_template, url_for, request, session
import secrets
from tempfile import mkdtemp
from flask_session import Session
from apps.gedo_app.gedoApp import *
from flask import Blueprint, current_app
gedoApp = Blueprint('gedoApp', __name__)


@gedoApp.route('/verNotas/GEDO/<int:codigo>', methods=["GET", "POST"])
def get_selected_content_gedo(codigo):
    return get_content_gedo(codigo)


@gedoApp.route('/nuevaSeccionGEDO/<int:codigo>', methods=["GET"])
def open_new_content_editor_gedo(codigo):
    return render_template("gedo_templates/nuevaSeccionGEDO.html", codigo=codigo)


@gedoApp.route('/uploadGEDO', methods=["POST"])
def upload_content_gedo():
    return post_new_content_gedo()


@gedoApp.route('/editarGEDO/<int:id>', methods=["GET", "POST"])
def edit_selected_content_gedo(id):
    return edit_content_gedo(id)
