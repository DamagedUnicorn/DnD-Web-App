from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def createApp():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'behsi8enh6abr09e'
	app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	db.init_app(app)

	from .views import views

	app.register_blueprint(views, url_prefix='/')

	from .models import Charactername

	create_database(app)


	return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
