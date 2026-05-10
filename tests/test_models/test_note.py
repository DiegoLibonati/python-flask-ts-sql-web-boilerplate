from datetime import datetime
from typing import Any

import pytest
from flask import Flask

from src.configs.sql_alchemy_config import db
from src.models.orm.note import Note


class TestNoteModel:
    @pytest.mark.unit
    def test_init_sets_content(self) -> None:
        note: Note = Note(content="hello")
        assert note.content == "hello"

    @pytest.mark.unit
    def test_init_sets_created_at_with_utc_timezone(self) -> None:
        note: Note = Note(content="x")
        assert note.created_at is not None
        assert isinstance(note.created_at, datetime)
        assert note.created_at.tzinfo is not None

    @pytest.mark.unit
    def test_to_dict_has_expected_keys(self) -> None:
        note: Note = Note(content="test")
        note.id = 1
        result: dict[str, Any] = note.to_dict()
        assert "id" in result
        assert "content" in result
        assert "created_at" in result

    @pytest.mark.unit
    def test_to_dict_values_match(self) -> None:
        note: Note = Note(content="hello")
        note.id = 5
        result: dict[str, Any] = note.to_dict()
        assert result["id"] == 5
        assert result["content"] == "hello"

    @pytest.mark.unit
    def test_to_dict_created_at_is_isoformat_string(self) -> None:
        note: Note = Note(content="x")
        note.id = 1
        result: dict[str, Any] = note.to_dict()
        assert isinstance(result["created_at"], str)
        datetime.fromisoformat(result["created_at"])

    @pytest.mark.integration
    def test_persisted_note_has_utc_timezone_after_load(self, app: Flask, db_session: None) -> None:
        note: Note = Note(content="persisted")
        db.session.add(note)
        db.session.commit()
        db.session.expire(note)
        reloaded: Note | None = db.session.get(Note, note.id)
        assert reloaded is not None
        assert reloaded.created_at.tzinfo is not None
