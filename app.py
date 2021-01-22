from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from config import AppConfig
from api import healthcheck_bp, address_bp


def create_app(app_config=AppConfig):
    app = Flask(__name__)
    app.config.from_object(app_config)
    app.register_blueprint(healthcheck_bp)
    app.register_blueprint(address_bp, url_prefix="/address")

    from database.db_models import db, ma
    db.init_app(app)
    ma.init_app(app)
    migrate = Migrate(app, db)  # noqa

    app.cli.add_command("db", MigrateCommand)
    return app
