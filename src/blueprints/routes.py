from flask import Flask

from src.blueprints.v1.note_bp import note_bp
from src.constants.vars import BLUEPRINT_NOTES_PATH


def register_routes(app: Flask) -> None:
    app.register_blueprint(note_bp, url_prefix=BLUEPRINT_NOTES_PATH)
