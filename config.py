import os

env = os.environ


class AppConfig:
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    ENV = env.get("FLASK_ENV", "production")
    SQLALCHEMY_DATABASE_URI = env.get("SQLALCHEMY_DATABASE_URI", f"sqlite:///{APP_DIR}/db.sqlite3")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
