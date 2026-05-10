import logging

import pytest

from src.configs.logger_config import setup_logger


class TestSetupLogger:
    @pytest.mark.unit
    def test_returns_logger_instance(self) -> None:
        logger: logging.Logger = setup_logger()
        assert isinstance(logger, logging.Logger)

    @pytest.mark.unit
    def test_default_name(self) -> None:
        logger: logging.Logger = setup_logger()
        assert logger.name == "python-flask-ts-sql-web-boilerplate"

    @pytest.mark.unit
    def test_custom_name(self) -> None:
        logger: logging.Logger = setup_logger("custom_logger")
        assert logger.name == "custom_logger"

    @pytest.mark.unit
    def test_logger_level_is_debug(self) -> None:
        logger: logging.Logger = setup_logger("test_level_logger")
        assert logger.level == logging.DEBUG

    @pytest.mark.unit
    def test_logger_has_at_least_one_handler(self) -> None:
        logger: logging.Logger = setup_logger("test_handler_logger")
        assert len(logger.handlers) >= 1

    @pytest.mark.unit
    def test_handler_is_stream_handler(self) -> None:
        logger: logging.Logger = setup_logger("test_stream_logger")
        assert any(isinstance(h, logging.StreamHandler) for h in logger.handlers)

    @pytest.mark.unit
    def test_calling_twice_does_not_add_duplicate_handlers(self) -> None:
        logger: logging.Logger = setup_logger("test_idempotent_logger")
        handler_count_first: int = len(logger.handlers)
        setup_logger("test_idempotent_logger")
        assert len(logger.handlers) == handler_count_first
