from flask import Flask
from routes.contact import contacts
from flask_sqlalchemy import SQLAlchemy
from config  import DATABASE_CONNECTION_URI
app = Flask(__name__)

app.secret_key = "Secret__key"

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_POOL_SIZE'] = 10
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 10
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 5
app.config['SQLALCHEMY_POOL_RECYCLE'] = 10

SQLAlchemy (app)

app.register_blueprint(contacts)
