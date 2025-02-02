from flask.templating import render_template
# from werkzeug.utils import redirect
from app.models import entry
from flask import Flask, flash, redirect, url_for
from werkzeug.exceptions import HTTPException
from flask_login import LoginManager
from config import Config
from .database import db, migrate

from .main.views import main
from .account.views import account
from .entry.views import entry

login = LoginManager()
login.login_view = 'account.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Alembic includes support for migrating a table in this way with a feature called "batch mode" - render_as_batch=True
    migrate.init_app(app, db, render_as_batch=True)
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

    @app.errorhandler(HTTPException)
    def handle_http_exception(err):
        '''
        Flash errors and redirect to index
        '''

        response = err.get_response()
        flash(response.status)

        return redirect(url_for('main.index'))


    app.register_blueprint(main)
    app.register_blueprint(account)
    app.register_blueprint(entry, url_prefix='/entry')

    return app
