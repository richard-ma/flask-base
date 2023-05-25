import os
from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass # instance folder exists

    @app.route("/")
    def index():
        return "hello world"

    return app

# run command: flask --app app:create_app run