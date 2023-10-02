from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_make_category = 'info'

from app.users.routes import users
from app.posts.routes import posts
from app.main.routes import main

app.register_blueprint(users) 
app.register_blueprint(posts) 
app.register_blueprint(main) 

with app.app_context(): # does this create a new db app reach time? 
    db.create_all()
