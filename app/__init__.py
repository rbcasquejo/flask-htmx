from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

with app.app_context():

    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///sqlite.db'
    app.config["SQLALCHEMY_ECHO"] = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db = SQLAlchemy()

    from app import views
    from app import models

    db.init_app(app)
    db.create_all()