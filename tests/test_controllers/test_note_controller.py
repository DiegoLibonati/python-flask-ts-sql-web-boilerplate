import json
from unittest.mock import patch

import pytest
from flask.testing import FlaskClient

from src.constants.codes import (
    CODE_NOT_FOUND_NOTE,
    CODE_NOT_VALID_FIELDS,
    CODE_NOT_VALID_INTEGER,
    CODE_SUCCESS_ADD_NOTE,
    CODE_SUCCESS_DELETE_NOTE,
    CODE_SUCCESS_EDIT_NOTE,
    CODE_SUCCESS_GET_ALL_NOTES,
)
from src.models.orm.note import Note


class TestNoteControllerAlive:
    @pytest.mark.unit
    def test_alive_returns_200(self, client: FlaskClient) -> None:
        response = client.get("/api/v1/notes/alive")
        assert response.status_code == 200

    @pytest.mark.unit
    def test_alive_returns_message(self, client: FlaskClient) -> None:
        response = client.get("/api/v1/notes/alive")
        data: dict[str, str] = json.loads(response.data)
        assert data["message"] == "I am Alive!"


class TestNoteControllerGetAll:
    @pytest.mark.unit
    def test_get_all_returns_200_with_empty_list(self, client: FlaskClient) -> None:
        with patch("src.controllers.note_controller.NoteService.get_all_notes", return_value=[]):
            response = client.get("/api/v1/notes/")
        assert response.status_code == 200
        data: dict = json.loads(response.data)
        assert data["code"] == CODE_SUCCESS_GET_ALL_NOTES
        assert data["data"] == []

    @pytest.mark.unit
    def test_get_all_returns_200_with_notes(self, client: FlaskClient) -> None:
        note: Note = Note(content="test note")
        note.id = 1
        with patch("src.controllers.note_controller.NoteService.get_all_notes", return_value=[note]):
            response = client.get("/api/v1/notes/")
        assert response.status_code == 200
        data: dict = json.loads(response.data)
        assert len(data["data"]) == 1
        assert data["data"][0]["content"] == "test note"


class TestNoteControllerCreate:
    @pytest.mark.unit
    def test_create_returns_201_with_valid_content(self, client: FlaskClient) -> None:
        note: Note = Note(content="created")
        note.id = 1
        with patch("src.controllers.note_controller.NoteService.add_note", return_value=note):
            response = client.post("/api/v1/notes/", json={"content": "created"})
        assert response.status_code == 201
        data: dict = json.loads(response.data)
        assert data["code"] == CODE_SUCCESS_ADD_NOTE

    @pytest.mark.unit
    def test_create_returns_400_with_empty_content(self, client: FlaskClient) -> None:
        response = client.post("/api/v1/notes/", json={"content": ""})
        assert response.status_code == 400
        data: dict = json.loads(response.data)
        assert data["code"] == CODE_NOT_VALID_FIELDS

    @pytest.mark.unit
    def test_create_returns_400_with_whitespace_content(self, client: FlaskClient) -> None:
        response = client.post("/api/v1/notes/", json={"content": "   "})
        assert response.status_code == 400
        data: dict = json.loads(response.data)
        assert data["code"] == CODE_NOT_VALID_FIELDS


class TestNoteControllerDelete:
    @pytest.mark.unit
    def test_delete_returns_200_when_note_exists(self, client: FlaskClient) -> None:
        note: Note = Note(content="to delete")
        note.id = 1
        with patch("src.controllers.note_controller.NoteService.get_note_by_id", return_value=note):
            with patch("src.controllers.note_controller.NoteService.delete_note"):
                response = client.delete("/api/v1/notes/1")
        assert response.status_code == 200
        data: dict = json.loads(response.data)
        assert data["code"] == CODE_SUCCESS_DELETE_NOTE

    @pytest.mark.unit
    def test_delete_returns_404_when_note_not_found(self, client: FlaskClient) -> None:
        with patch("src.controllers.note_controller.NoteService.get_note_by_id", return_value=None):
            response = client.delete("/api/v1/notes/1")
        assert response.status_code == 404
        data: dict = json.loads(response.data)
        assert data["code"] == CODE_NOT_FOUND_NOTE

    @pytest.mark.unit
    def test_delete_returns_400_with_non_integer_id(self, client: FlaskClient) -> None:
        response = client.delete("/api/v1/notes/abc")
        assert response.status_code == 400
        data: dict = json.loads(response.data)
        assert data["code"] == CODE_NOT_VALID_INTEGER


class TestNoteControllerEdit:
    @pytest.mark.unit
    def test_edit_returns_200_when_valid(self, client: FlaskClient) -> None:
        note: Note = Note(content="original")
        note.id = 1
        with patch("src.controllers.note_controller.NoteService.get_note_by_id", return_value=note):
            with patch("src.controllers.note_controller.NoteService.update_note"):
                response = client.patch("/api/v1/notes/1", json={"content": "updated"})
        assert response.status_code == 200
        data: dict = json.loads(response.data)
        assert data["code"] == CODE_SUCCESS_EDIT_NOTE

    @pytest.mark.unit
    def test_edit_returns_400_with_non_integer_id(self, client: FlaskClient) -> None:
        response = client.patch("/api/v1/notes/abc", json={"content": "x"})
        assert response.status_code == 400
        data: dict = json.loads(response.data)
        assert data["code"] == CODE_NOT_VALID_INTEGER

    @pytest.mark.unit
    def test_edit_returns_400_with_empty_content(self, client: FlaskClient) -> None:
        response = client.patch("/api/v1/notes/1", json={"content": ""})
        assert response.status_code == 400
        data: dict = json.loads(response.data)
        assert data["code"] == CODE_NOT_VALID_FIELDS

    @pytest.mark.unit
    def test_edit_returns_404_when_note_not_found(self, client: FlaskClient) -> None:
        with patch("src.controllers.note_controller.NoteService.get_note_by_id", return_value=None):
            response = client.patch("/api/v1/notes/1", json={"content": "x"})
        assert response.status_code == 404
        data: dict = json.loads(response.data)
        assert data["code"] == CODE_NOT_FOUND_NOTE
