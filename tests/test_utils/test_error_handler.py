from unittest.mock import patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from src.constants.codes import CODE_ERROR_DATABASE, CODE_ERROR_GENERIC
from src.utils.error_handler import handle_exceptions
from src.utils.exceptions import BaseAPIError, InternalAPIError, ValidationAPIError


class TestHandleExceptions:
    @pytest.mark.unit
    def test_returns_function_result_when_no_exception(self) -> None:
        @handle_exceptions
        def fn() -> int:
            return 42

        result: int = fn()
        assert result == 42

    @pytest.mark.unit
    def test_preserves_function_name_via_wraps(self) -> None:
        @handle_exceptions
        def my_function() -> None:
            pass

        assert my_function.__name__ == "my_function"

    @pytest.mark.unit
    def test_passes_through_base_api_error(self) -> None:
        @handle_exceptions
        def fn() -> None:
            raise ValidationAPIError(code="TEST", message="test error")

        with pytest.raises(ValidationAPIError):
            fn()

    @pytest.mark.unit
    def test_wraps_sqlalchemy_error_as_internal_api_error(self) -> None:
        @handle_exceptions
        def fn() -> None:
            raise SQLAlchemyError("db fail")

        with patch("src.utils.error_handler.logger"):
            with pytest.raises(InternalAPIError) as exc_info:
                fn()
        assert exc_info.value.code == CODE_ERROR_DATABASE

    @pytest.mark.unit
    def test_wraps_generic_exception_as_internal_api_error(self) -> None:
        @handle_exceptions
        def fn() -> None:
            raise RuntimeError("unexpected")

        with patch("src.utils.error_handler.logger"):
            with pytest.raises(InternalAPIError) as exc_info:
                fn()
        assert exc_info.value.code == CODE_ERROR_GENERIC

    @pytest.mark.unit
    def test_sqlalchemy_error_result_is_base_api_error(self) -> None:
        @handle_exceptions
        def fn() -> None:
            raise SQLAlchemyError("db fail")

        with patch("src.utils.error_handler.logger"):
            with pytest.raises(BaseAPIError):
                fn()

    @pytest.mark.unit
    def test_passes_args_to_wrapped_function(self) -> None:
        @handle_exceptions
        def fn(a: int, b: int) -> int:
            return a + b

        result: int = fn(2, 3)
        assert result == 5
