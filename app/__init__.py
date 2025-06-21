from flask import Flask
from .controllers.home_controller import home_bp
from .database import db
from flask_migrate import Migrate
from .constants.config import  db_url,env

migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = db_url

    db.init_app(app)
    migrate.init_app(app,db)

    app.register_blueprint(home_bp)

    with app.app_context():
        from .database import models

    return app
