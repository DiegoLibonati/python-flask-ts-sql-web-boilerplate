from unittest.mock import patch

import pytest

from src.models.orm.note import Note
from src.services.note_service import NoteService


class TestNoteService:
    @pytest.mark.unit
    def test_get_all_notes_returns_list(self) -> None:
        mock_notes: list[Note] = [Note(content="a"), Note(content="b")]
        with patch("src.services.note_service.NoteDAO.query_all", return_value=mock_notes):
            result: list[Note] = NoteService.get_all_notes()
        assert len(result) == 2

    @pytest.mark.unit
    def test_get_all_notes_returns_empty_list(self) -> None:
        with patch("src.services.note_service.NoteDAO.query_all", return_value=[]):
            result: list[Note] = NoteService.get_all_notes()
        assert result == []

    @pytest.mark.unit
    def test_get_note_by_id_returns_note(self) -> None:
        expected: Note = Note(content="found")
        with patch("src.services.note_service.NoteDAO.query_by_id", return_value=expected):
            result: Note | None = NoteService.get_note_by_id(1)
        assert result is expected

    @pytest.mark.unit
    def test_get_note_by_id_returns_none(self) -> None:
        with patch("src.services.note_service.NoteDAO.query_by_id", return_value=None):
            result: Note | None = NoteService.get_note_by_id(99)
        assert result is None

    @pytest.mark.unit
    def test_add_note_calls_dao_and_returns_note(self) -> None:
        note: Note = Note(content="new")
        with patch("src.services.note_service.NoteDAO.add", return_value=note) as mock_add:
            result: Note = NoteService.add_note(note)
        mock_add.assert_called_once_with(note)
        assert result is note

    @pytest.mark.unit
    def test_delete_note_calls_dao(self) -> None:
        note: Note = Note(content="del")
        with patch("src.services.note_service.NoteDAO.delete") as mock_delete:
            NoteService.delete_note(note)
        mock_delete.assert_called_once_with(note)

    @pytest.mark.unit
    def test_update_note_calls_dao(self) -> None:
        note: Note = Note(content="old")
        data: dict[str, str] = {"content": "new"}
        with patch("src.services.note_service.NoteDAO.update") as mock_update:
            NoteService.update_note(note, data)
        mock_update.assert_called_once_with(note, data)
