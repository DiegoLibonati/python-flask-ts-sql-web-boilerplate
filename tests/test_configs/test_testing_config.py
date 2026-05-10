import pytest

from src.configs.testing_config import TestingConfig


class TestTestingConfig:
    @pytest.mark.unit
    def test_testing_flag_is_true(self) -> None:
        assert TestingConfig.TESTING is True

    @pytest.mark.unit
    def test_debug_flag_is_true(self) -> None:
        assert TestingConfig.DEBUG is True

    @pytest.mark.unit
    def test_database_uri_is_sqlite_in_memory(self) -> None:
        assert TestingConfig.SQLALCHEMY_DATABASE_URI == "sqlite:///:memory:"

    @pytest.mark.unit
    def test_secret_key_is_set(self) -> None:
        assert TestingConfig.SECRET_KEY == "testing-secret-key"

    @pytest.mark.unit
    def test_sqlalchemy_track_modifications_is_false(self) -> None:
        assert TestingConfig.SQLALCHEMY_TRACK_MODIFICATIONS is False
