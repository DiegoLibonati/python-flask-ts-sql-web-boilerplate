from typing import Any

import pytest
from flask import Flask

from src.constants.codes import CODE_ERROR_INTERNAL_SERVER
from src.constants.messages import MESSAGE_ERROR_INTERNAL_SERVER
from src.utils.exceptions import (
    BaseAPIError,
    BusinessAPIError,
    ConflictAPIError,
    InternalAPIError,
    NotFoundAPIError,
    ValidationAPIError,
)


class TestBaseAPIError:
    @pytest.mark.unit
    def test_default_status_code_is_500(self) -> None:
        error: BaseAPIError = BaseAPIError()
        assert error.status_code == 500

    @pytest.mark.unit
    def test_default_message(self) -> None:
        error: BaseAPIError = BaseAPIError()
        assert error.message == MESSAGE_ERROR_INTERNAL_SERVER

    @pytest.mark.unit
    def test_default_code(self) -> None:
        error: BaseAPIError = BaseAPIError()
        assert error.code == CODE_ERROR_INTERNAL_SERVER

    @pytest.mark.unit
    def test_custom_status_code(self) -> None:
        error: BaseAPIError = BaseAPIError(status_code=422)
        assert error.status_code == 422

    @pytest.mark.unit
    def test_custom_message(self) -> None:
        error: BaseAPIError = BaseAPIError(message="custom message")
        assert error.message == "custom message"

    @pytest.mark.unit
    def test_custom_code(self) -> None:
        error: BaseAPIError = BaseAPIError(code="CUSTOM_CODE")
        assert error.code == "CUSTOM_CODE"

    @pytest.mark.unit
    def test_to_dict_returns_code_and_message(self) -> None:
        error: BaseAPIError = BaseAPIError(code="ERR", message="msg")
        result: dict[str, Any] = error.to_dict()
        assert result["code"] == "ERR"
        assert result["message"] == "msg"

    @pytest.mark.unit
    def test_to_dict_excludes_payload_when_empty(self) -> None:
        error: BaseAPIError = BaseAPIError()
        result: dict[str, Any] = error.to_dict()
        assert "payload" not in result

    @pytest.mark.unit
    def test_to_dict_includes_payload_when_present(self) -> None:
        payload: dict[str, str] = {"field": "value"}
        error: BaseAPIError = BaseAPIError(payload=payload)
        result: dict[str, Any] = error.to_dict()
        assert "payload" in result
        assert result["payload"]["field"] == "value"

    @pytest.mark.unit
    def test_flask_response_status_matches(self, app: Flask) -> None:
        error: BaseAPIError = BaseAPIError(status_code=422)
        with app.app_context():
            _, status = error.flask_response()
        assert status == 422

    @pytest.mark.unit
    def test_flask_response_default_status_is_500(self, app: Flask) -> None:
        error: BaseAPIError = BaseAPIError()
        with app.app_context():
            _, status = error.flask_response()
        assert status == 500

    @pytest.mark.unit
    def test_is_exception(self) -> None:
        error: BaseAPIError = BaseAPIError()
        assert isinstance(error, Exception)


class TestValidationAPIError:
    @pytest.mark.unit
    def test_status_code_is_400(self) -> None:
        assert ValidationAPIError.status_code == 400

    @pytest.mark.unit
    def test_inherits_from_base_api_error(self) -> None:
        assert issubclass(ValidationAPIError, BaseAPIError)


class TestNotFoundAPIError:
    @pytest.mark.unit
    def test_status_code_is_404(self) -> None:
        assert NotFoundAPIError.status_code == 404

    @pytest.mark.unit
    def test_inherits_from_base_api_error(self) -> None:
        assert issubclass(NotFoundAPIError, BaseAPIError)


class TestConflictAPIError:
    @pytest.mark.unit
    def test_status_code_is_409(self) -> None:
        assert ConflictAPIError.status_code == 409


class TestBusinessAPIError:
    @pytest.mark.unit
    def test_status_code_is_422(self) -> None:
        assert BusinessAPIError.status_code == 422


class TestInternalAPIError:
    @pytest.mark.unit
    def test_status_code_is_500(self) -> None:
        assert InternalAPIError.status_code == 500
