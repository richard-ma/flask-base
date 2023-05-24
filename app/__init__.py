from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route("/")
    def index():
        return "hello world"

    return app

# run command: flask --app app:create_app run