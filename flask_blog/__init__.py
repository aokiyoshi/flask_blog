from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from flask_blog.config import Config


db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    # Создаем приложение и загружаем конфиг
    app = Flask(__name__)
    app.config.from_object(Config)

    # Инициализируем приложение
    db.init_app(app)
    login_manager.init_app(app)


    # Инициализируем руты
    from flask_blog.main.routes import main
    app.register_blueprint(main)

    # Возвращаем приложение
    return app
