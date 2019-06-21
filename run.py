from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app= Flask(__name__)

    app.config['SQALCHEMY_DATABASE_URI'] = 'sqlite:///api_demo.bd'

    from .view import main
    app.register_blueprint(main)
    

    return app
