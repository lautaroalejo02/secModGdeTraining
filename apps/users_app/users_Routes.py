from flask import Flask, flash, jsonify, redirect, render_template, url_for, request, session
import secrets
from tempfile import mkdtemp
from flask_session import Session
from apps.users_app.usersApp import *
from flask import Blueprint, current_app
usersApp = Blueprint('usersApp', __name__)


@usersApp.route("/register", methods=["GET", "POST"])
def register():
    return register_user()


@usersApp.route('/login', methods=["GET", "POST"])
def login_user():
    return login()


@usersApp.route('/logout', methods=["GET", "POST"])
def logout_user():
    return logout()


@usersApp.route('/adminUsers', methods=["GET", "POST"])
def all_users():
    return get_all_users()


@usersApp.route('/modificarU/<int:id>', methods=["GET", "POST"])
def get_user_to_modify(id):
    return get_user_by_id(id)


@usersApp.route('/modificarPostU', methods=["POST"])
def modificar_usuario_post():
    return modify_user()


@usersApp.route('/eliminar/<int:id>', methods=["GET", "POST"])
def delete_selected_userd(id):
    return delete_user(id)


@usersApp.route('/encuesta', methods=["GET", "POST"])
def user_survey():
    return survey()


@usersApp.route('/verEncuesta', methods=["GET", "POST"])
def get_all_surveys():
    return all_surveys()


@usersApp.route('/borrar/<int:id>', methods=["GET", "POST"])
def delete_selected_survey(id):
    return delete_survey(id)
