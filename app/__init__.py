from flask import Flask



print("hello world")
def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')

    from .routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    return app