from cs50 import SQL
import sqlite3
from flask import Flask, flash, jsonify, redirect, render_template, url_for, request, session
import secrets
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from flask_session import Session
from flask_mail import Mail, Message
from flask import Blueprint, current_app
from database_init import db
app = Flask(__name__)
gedoManager = Blueprint('gedoManager', __name__)
#db = SQL('sqlite:///courseGDE6.db')

url = "mysql://root:@localhost:3308/coursegde7"
db = SQL(url, pool_recycle=299)


if __name__ == "__main__":
    gedoManager.run(debug=True)
