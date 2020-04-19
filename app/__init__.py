from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from flask_login import LoginManager

myApp = Flask(__name__)
myApp.config.from_object(Config)
myDB = SQLAlchemy(myApp)
migrate = Migrate(myApp, myDB)
login = LoginManager(myApp)
login.login_view = 'login'

from app import routes, models

