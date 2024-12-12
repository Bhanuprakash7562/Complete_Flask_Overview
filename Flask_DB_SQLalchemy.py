from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

def createApp():
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./testdb.db'
    # In case of MySQL ==> app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
    app.secret_key = 'SOME KEY'

    db.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app=app)
    
    # Note: In case if you import model and views globally it will cause circularimport error..!
    from model import User
    @login_manager.user_loader
    def load_user(uid):
        return User.query.get(uid)
    
    bcrypt = Bcrypt(app=app)

    from views import register_views, login_page
    # register_views(app=app, db=db)
    login_page(app=app, db=db, bcrypt=bcrypt)

    migrate = Migrate(app, db)
    return app