from unittest.mock import patch

import pytest
from flask import Flask

from src.configs.sql_alchemy_config import db
from src.data_access.note_dao import NoteDAO
from src.models.orm.note import Note


class TestNoteDAO:
    @pytest.mark.integration
    def test_query_all_returns_empty_list(self, app: Flask, db_session: None) -> None:
        result: list[Note] = NoteDAO.query_all()
        assert result == []

    @pytest.mark.integration
    def test_query_all_returns_notes(self, app: Flask, db_session: None) -> None:
        db.session.add(Note(content="hello"))
        db.session.commit()
        result: list[Note] = NoteDAO.query_all()
        assert len(result) == 1
        assert result[0].content == "hello"

    @pytest.mark.integration
    def test_query_by_id_returns_note(self, app: Flask, db_session: None) -> None:
        note: Note = Note(content="find me")
        db.session.add(note)
        db.session.commit()
        result: Note | None = NoteDAO.query_by_id(note.id)
        assert result is not None
        assert result.content == "find me"

    @pytest.mark.integration
    def test_query_by_id_returns_none_when_missing(self, app: Flask, db_session: None) -> None:
        result: Note | None = NoteDAO.query_by_id(99999)
        assert result is None

    @pytest.mark.integration
    def test_add_persists_note(self, app: Flask, db_session: None) -> None:
        note: Note = Note(content="new note")
        result: Note = NoteDAO.add(note)
        assert result.id is not None
        assert result.content == "new note"

    @pytest.mark.integration
    def test_update_changes_content(self, app: Flask, db_session: None) -> None:
        note: Note = Note(content="original")
        NoteDAO.add(note)
        NoteDAO.update(note, {"content": "updated"})
        reloaded: Note | None = NoteDAO.query_by_id(note.id)
        assert reloaded is not None
        assert reloaded.content == "updated"

    @pytest.mark.integration
    def test_update_rollbacks_on_exception(self, app: Flask, db_session: None) -> None:
        note: Note = Note(content="x")
        NoteDAO.add(note)
        with patch("src.data_access.note_dao.logger"):
            with patch.object(db.session, "commit", side_effect=Exception("db fail")):
                with pytest.raises(Exception):
                    NoteDAO.update(note, {"content": "y"})

    @pytest.mark.integration
    def test_delete_removes_note(self, app: Flask, db_session: None) -> None:
        note: Note = Note(content="remove me")
        NoteDAO.add(note)
        note_id: int = note.id
        NoteDAO.delete(note)
        assert NoteDAO.query_by_id(note_id) is None

    @pytest.mark.integration
    def test_delete_rollbacks_on_exception(self, app: Flask, db_session: None) -> None:
        note: Note = Note(content="x")
        NoteDAO.add(note)
        with patch("src.data_access.note_dao.logger"):
            with patch.object(db.session, "commit", side_effect=Exception("db fail")):
                with pytest.raises(Exception):
                    NoteDAO.delete(note)
