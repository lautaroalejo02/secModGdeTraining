from cs50 import SQL
import sqlite3
from flask import Flask, flash, jsonify, redirect, render_template, url_for, request, session
import secrets
import requests
import sys
from tempfile import mkdtemp
from flask_session import Session
from database_init import db
from flask_mail import Mail, Message
app = Flask(__name__)


def error(message, code=400):
    return render_template("helpers_templates/error.html", message=(message), code=code)


def exito(message):
    return render_template("helpers_templates/exito.html", message=(message))


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'secmodgdesender@gmail.com'
app.config['MAIL_PASSWORD'] = 'modernizacion55'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

# remember that i downgraded flask_mail from 0.9.1 to 0.9.0


def send_email(mail_body, mail_html, mail_subject, mail_recipient):
    print("hola")
    msg = Message('hola', sender='secmodgdesender@gmail.com',
                  recipients=[mail_recipient])
    msg.body = mail_body
    msg.html = mail_html
    msg.subject = mail_subject
    mail.send(msg)
