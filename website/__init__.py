from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from os import path
from flask_login import LoginManager

db=SQLAlchemy()
login_manager = LoginManager()
DB_NAME = "database.db"

#Use this to create flask app
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Something to not share'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    
    


    #We defined those blueprints we need to register them to flask
    from .views import views
    from .auth import auth
    
    
    app.register_blueprint(views, url_prefix = "/") #prefix/route is the real route 
    app.register_blueprint(auth, url_prefix = "/")
    
    
    from .models import User, Note
    
    create_database(app)
    
    
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    
    return app
def create_database(app):
    if not path.exists("website/" + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Databse!')
        