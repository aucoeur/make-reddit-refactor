from app.models import entry
from flask import Flask
from flask_login import LoginManager
from config import Config
from .database import db, migrate

from .main.views import main
from .account.views import account
from .entry.views import entry

login = LoginManager()
login.login_view = 'login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    migrate.init_app(app, db)
    login.init_app(app)

    from app.models import Entry, User
    
    @app.shell_context_processor
    def make_shell_context():
        '''
        Creates a shell context that pre-imports the database instance and models to the shell session when using `flask shell`
        '''
        return {'db': db, 'User': User, 'Entry': Entry}

    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

    app.register_blueprint(main)
    app.register_blueprint(account)
    app.register_blueprint(entry, url_prefix='/entry')

    return app