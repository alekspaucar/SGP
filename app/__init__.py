

from flask import Flask


print("hello world Empezando...")



def create_app():
    app = Flask(__name__)

    from .routes.main import main
    app.register_blueprint(main)

    return app