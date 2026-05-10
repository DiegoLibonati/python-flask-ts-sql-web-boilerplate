from unittest.mock import patch

import pytest
from flask.testing import FlaskClient

from src.models.orm.note import Note


class TestAppViewHome:
    @pytest.mark.unit
    def test_home_returns_200(self, client: FlaskClient) -> None:
        with patch("src.views.v1.app_view.NoteService.get_all_notes", return_value=[]):
            with patch("src.views.v1.app_view.render_template", return_value="<html></html>"):
                response = client.get("/views/v1/app/home")
        assert response.status_code == 200

    @pytest.mark.unit
    def test_home_returns_html_content_type(self, client: FlaskClient) -> None:
        with patch("src.views.v1.app_view.NoteService.get_all_notes", return_value=[]):
            with patch("src.views.v1.app_view.render_template", return_value="<html></html>"):
                response = client.get("/views/v1/app/home")
        assert response.content_type.startswith("text/html")

    @pytest.mark.unit
    def test_home_calls_get_all_notes(self, client: FlaskClient) -> None:
        with patch("src.views.v1.app_view.NoteService.get_all_notes", return_value=[]) as mock_get:
            with patch("src.views.v1.app_view.render_template", return_value="<html></html>"):
                client.get("/views/v1/app/home")
        mock_get.assert_called_once()

    @pytest.mark.unit
    def test_home_passes_notes_to_template(self, client: FlaskClient) -> None:
        note: Note = Note(content="visible content")
        note.id = 1
        with patch("src.views.v1.app_view.NoteService.get_all_notes", return_value=[note]):
            with patch("src.views.v1.app_view.render_template", return_value="<html></html>") as mock_render:
                client.get("/views/v1/app/home")
        _, kwargs = mock_render.call_args
        context: dict = kwargs.get("context", {})
        assert note in context["notes"]

    @pytest.mark.unit
    def test_unknown_url_redirects_to_home(self, client: FlaskClient) -> None:
        response = client.get("/this-does-not-exist")
        assert response.status_code == 302
        assert "/views/v1/app/home" in response.location
