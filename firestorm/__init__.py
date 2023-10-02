from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from firestorm.config import Config 


db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_make_category = 'info'


def create_app(config_class=Config):
    
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app,db)
    login_manager.init_app(app)


    from firestorm.users.routes import users
    from firestorm.posts.routes import posts
    from firestorm.main.routes import main
    from firestorm.errors.handlers import errors # importing intance of the blueprint 
    app.register_blueprint(users) 
    app.register_blueprint(posts) 
    app.register_blueprint(main) 
    app.register_blueprint(errors) # register the blueprint 

    return app