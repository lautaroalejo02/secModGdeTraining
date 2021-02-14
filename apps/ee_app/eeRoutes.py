from flask import Flask, flash, jsonify, redirect, render_template, url_for, request, session
import secrets
from tempfile import mkdtemp
from flask_session import Session
from apps.ee_app.eeApp import *
from flask import Blueprint, current_app
eeApp = Blueprint('eeApp', __name__)


@eeApp.route('/verNotas/EE/<int:codigo>', methods=["GET"])
def get_selected_content_ee(codigo):
    return get_content_ee(codigo)


@eeApp.route('/nuevaSeccionEE/<int:codigo>')
def open_new_content_editor_ee(codigo):
    return render_template("ee_templates/nuevaSeccionEE.html", codigo=codigo)


@eeApp.route('/uploadEE', methods=["POST"])
def upload_content_ee():
    return post_new_content_ee()


@eeApp.route('/editarEE/<int:codigo>', methods=["GET", "POST"])
def edit_selected_content_ee(codigo):
    return edit_content_ee(codigo)
