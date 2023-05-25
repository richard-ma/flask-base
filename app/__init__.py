import os
import logging
from logging.handlers import RotatingFileHandler
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
        log_filename = 'development.log'
        log_level = logging.DEBUG
    elif e == 'testing':
        cfg_name = 'config.TestingConfig'
        log_filename = 'testing.log'
        log_level = logging.DEBUG
    else: # production as default
        cfg_name = 'config.ProductionConfig'
        log_filename = 'production.log'
        log_level = logging.WARNING

    # add logging handler
    rotating_file_handler = RotatingFileHandler(
        os.path.join(app.instance_path, log_filename),
        maxBytes=20000000,
        backupCount=10,
    )
    # add handler to logger
    for logger in (app.logger, ):
        logger.addHandler(rotating_file_handler)
        logger.setLevel(log_level)

    app.logger.debug("Loading Configration: " + cfg_name)
    cfg = import_string(cfg_name)()
    app.logger.debug("Configration loaded: " + str(cfg))
    app.config.from_object(cfg)

    @app.route("/")
    def index():
        return "hello world"

    return app

# run command: flask --app app:create_app run