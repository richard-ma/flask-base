import os
from flask import Flask
from werkzeug.utils import import_string


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass # instance folder exists

    # get flask environment variable
    e = os.environ.get('FLASK_ENV', 'production') # default flask environment is production

    # load configration
    if e == 'dev':
        cfg_name = 'config.DevelopmentConfig'
    elif e == 'testing':
        cfg_name = 'config.TestingConfig'
    else: # production as default
        cfg_name = 'config.ProductionConfig'
    cfg = import_string(cfg_name)()
    app.config.from_object(cfg)

    @app.route("/")
    def index():
        return "hello world"

    return app

# run command: flask --app app:create_app run