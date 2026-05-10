import pytest

from src.constants.codes import (
    CODE_ALREADY_EXISTS_NOTE,
    CODE_ERROR_DATABASE,
    CODE_ERROR_GENERIC,
    CODE_ERROR_INTERNAL_SERVER,
    CODE_NOT_FOUND_NOTE,
    CODE_NOT_VALID_FIELDS,
    CODE_NOT_VALID_INTEGER,
    CODE_SUCCESS_ADD_NOTE,
    CODE_SUCCESS_DELETE_NOTE,
    CODE_SUCCESS_EDIT_NOTE,
    CODE_SUCCESS_GET_ALL_NOTES,
    FLASH_ERROR,
    FLASH_SUCCESS,
)


class TestFlashCodes:
    @pytest.mark.unit
    def test_flash_success_value(self) -> None:
        assert FLASH_SUCCESS == "success"

    @pytest.mark.unit
    def test_flash_error_value(self) -> None:
        assert FLASH_ERROR == "error"


class TestSuccessCodes:
    @pytest.mark.unit
    def test_all_success_codes_are_strings(self) -> None:
        codes: list[str] = [
            CODE_SUCCESS_GET_ALL_NOTES,
            CODE_SUCCESS_ADD_NOTE,
            CODE_SUCCESS_DELETE_NOTE,
            CODE_SUCCESS_EDIT_NOTE,
        ]
        assert all(isinstance(c, str) for c in codes)

    @pytest.mark.unit
    def test_all_success_codes_start_with_success(self) -> None:
        codes: list[str] = [
            CODE_SUCCESS_GET_ALL_NOTES,
            CODE_SUCCESS_ADD_NOTE,
            CODE_SUCCESS_DELETE_NOTE,
            CODE_SUCCESS_EDIT_NOTE,
        ]
        assert all(c.startswith("SUCCESS_") for c in codes)


class TestErrorCodes:
    @pytest.mark.unit
    def test_all_error_codes_are_strings(self) -> None:
        codes: list[str] = [
            CODE_ERROR_INTERNAL_SERVER,
            CODE_ERROR_DATABASE,
            CODE_ERROR_GENERIC,
            CODE_NOT_VALID_INTEGER,
            CODE_NOT_VALID_FIELDS,
            CODE_NOT_FOUND_NOTE,
            CODE_ALREADY_EXISTS_NOTE,
        ]
        assert all(isinstance(c, str) for c in codes)

    @pytest.mark.unit
    def test_codes_are_unique(self) -> None:
        codes: list[str] = [
            CODE_SUCCESS_GET_ALL_NOTES,
            CODE_SUCCESS_ADD_NOTE,
            CODE_SUCCESS_DELETE_NOTE,
            CODE_SUCCESS_EDIT_NOTE,
            CODE_ERROR_INTERNAL_SERVER,
            CODE_ERROR_DATABASE,
            CODE_ERROR_GENERIC,
            CODE_NOT_VALID_INTEGER,
            CODE_NOT_VALID_FIELDS,
            CODE_NOT_FOUND_NOTE,
            CODE_ALREADY_EXISTS_NOTE,
        ]
        assert len(codes) == len(set(codes))
