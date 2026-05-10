from flask import Blueprint, Response, current_app, render_template

from src.constants.paths import RENDER_TEMPLATE_HOME_PATH
from src.services.note_service import NoteService
from src.utils.helpers import get_context_by_key

app_view = Blueprint("app_view", __name__, template_folder="templates")


@app_view.route("/home", methods=["GET"])
def home() -> Response:
    notes = NoteService.get_all_notes()
    context = get_context_by_key(app=current_app, key="home", notes=notes)

    return render_template(RENDER_TEMPLATE_HOME_PATH, context=context)
