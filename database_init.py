from cs50 import SQL
import sqlite3
import secrets
from flask_session import Session

url = "mysql://root:@localhost:3308/coursegde7"
db = SQL(url, pool_recycle=299)
