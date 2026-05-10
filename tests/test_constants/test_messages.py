import pytest

from src.constants.messages import (
    MESSAGE_ALREADY_EXISTS_NOTE,
    MESSAGE_ERROR_DATABASE,
    MESSAGE_ERROR_GENERIC,
    MESSAGE_ERROR_INTERNAL_SERVER,
    MESSAGE_NOT_FOUND_NOTE,
    MESSAGE_NOT_VALID_FIELDS,
    MESSAGE_NOT_VALID_INTEGER,
    MESSAGE_SUCCESS_ADD_NOTE,
    MESSAGE_SUCCESS_DELETE_NOTE,
    MESSAGE_SUCCESS_EDIT_NOTE,
    MESSAGE_SUCCESS_GET_ALL_NOTES,
)


class TestSuccessMessages:
    @pytest.mark.unit
    def test_all_success_messages_are_strings(self) -> None:
        messages: list[str] = [
            MESSAGE_SUCCESS_GET_ALL_NOTES,
            MESSAGE_SUCCESS_ADD_NOTE,
            MESSAGE_SUCCESS_DELETE_NOTE,
            MESSAGE_SUCCESS_EDIT_NOTE,
        ]
        assert all(isinstance(m, str) for m in messages)

    @pytest.mark.unit
    def test_all_success_messages_are_non_empty(self) -> None:
        messages: list[str] = [
            MESSAGE_SUCCESS_GET_ALL_NOTES,
            MESSAGE_SUCCESS_ADD_NOTE,
            MESSAGE_SUCCESS_DELETE_NOTE,
            MESSAGE_SUCCESS_EDIT_NOTE,
        ]
        assert all(len(m) > 0 for m in messages)


class TestErrorMessages:
    @pytest.mark.unit
    def test_all_error_messages_are_strings(self) -> None:
        messages: list[str] = [
            MESSAGE_ERROR_INTERNAL_SERVER,
            MESSAGE_ERROR_DATABASE,
            MESSAGE_ERROR_GENERIC,
            MESSAGE_NOT_VALID_INTEGER,
            MESSAGE_NOT_VALID_FIELDS,
            MESSAGE_NOT_FOUND_NOTE,
            MESSAGE_ALREADY_EXISTS_NOTE,
        ]
        assert all(isinstance(m, str) for m in messages)

    @pytest.mark.unit
    def test_all_error_messages_are_non_empty(self) -> None:
        messages: list[str] = [
            MESSAGE_ERROR_INTERNAL_SERVER,
            MESSAGE_ERROR_DATABASE,
            MESSAGE_ERROR_GENERIC,
            MESSAGE_NOT_VALID_INTEGER,
            MESSAGE_NOT_VALID_FIELDS,
            MESSAGE_NOT_FOUND_NOTE,
            MESSAGE_ALREADY_EXISTS_NOTE,
        ]
        assert all(len(m) > 0 for m in messages)
