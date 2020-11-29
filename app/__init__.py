from flask import Flask
from config import Config
from .database import db, migrate
from .models import Post, User

from .main.views import main
from .account.views import account


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    @app.shell_context_processor
    def make_shell_context():
        '''
        Creates a shell context that pre-imports the database instance and models to the shell session when using `flask shell`
        '''
        return {'db': db, 'User': User, 'Post': Post}

    app.register_blueprint(main)
    app.register_blueprint(account)

    return app


# def reset_db(app):
#     ''' Assumes you have imported all your db models already 
#     '''
# 
#     with app.app_context():
#         db.drop_all()
#         db.create_all()
#     db.session.commit()