from flask import Flask
from .extensions import db, migrate
from .quest import quest_bp
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(quest_bp, url_prefix ="/")
    from . import models

    return app

