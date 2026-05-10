import pytest

from src.configs.default_config import DefaultConfig
from src.configs.development_config import DevelopmentConfig


class TestDevelopmentConfig:
    @pytest.mark.unit
    def test_debug_is_true(self) -> None:
        assert DevelopmentConfig.DEBUG is True

    @pytest.mark.unit
    def test_testing_is_false(self) -> None:
        assert DevelopmentConfig.TESTING is False

    @pytest.mark.unit
    def test_inherits_from_default_config(self) -> None:
        assert issubclass(DevelopmentConfig, DefaultConfig)

    @pytest.mark.unit
    def test_sqlalchemy_track_modifications_is_false(self) -> None:
        assert DevelopmentConfig.SQLALCHEMY_TRACK_MODIFICATIONS is False

    @pytest.mark.unit
    def test_database_uri_uses_mysql_driver(self) -> None:
        assert DevelopmentConfig.SQLALCHEMY_DATABASE_URI.startswith("mysql+pymysql://")
