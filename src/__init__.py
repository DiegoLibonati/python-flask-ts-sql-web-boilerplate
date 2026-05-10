import importlib

from flask import Flask, redirect, url_for
from flask_migrate import Migrate

from src.blueprints.routes import register_routes
from src.configs.logger_config import setup_logger
from src.configs.sql_alchemy_config import db
from src.utils.exceptions import BaseAPIError
from src.views.routes import register_views

logger = setup_logger()


def create_app(config_name="development"):
    app = Flask(__name__)

    config_module = importlib.import_module(f"src.configs.{config_name}_config")
    app.config.from_object(config_module.__dict__[f"{config_name.capitalize()}Config"])

    db.init_app(app)
    Migrate(app, db)

    register_routes(app)

    register_views(app)

    @app.errorhandler(BaseAPIError)
    def handle_api_error(error: BaseAPIError):
        return error.flask_response()

    @app.errorhandler(404)
    def page_not_found(_):
        return redirect(url_for(app.config["HOME_VIEW"]))

    app.jinja_env.add_extension("jinja2.ext.loopcontrols")

    return app
