from flask_login import LoginManager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "sjsjberksj"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from . auth import auth
    from . views import views
    
    from .models import User,Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    app.register_blueprint(auth)
    app.register_blueprint(views)
    
    return app

def create_database(app):
    if not path.exists("Flaskr/" + DB_NAME):
        db.create_all(app=app)
        print("\n \n \n \n ohh oldu database")

# $env:FLASK_APP = "flaskr"
# $env:FLASK_ENV = "development"
# flask run
#


