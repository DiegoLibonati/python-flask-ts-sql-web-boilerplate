import pytest

from src.configs.default_config import DefaultConfig
from src.configs.production_config import ProductionConfig


class TestProductionConfig:
    @pytest.mark.unit
    def test_debug_is_false(self) -> None:
        assert ProductionConfig.DEBUG is False

    @pytest.mark.unit
    def test_testing_is_false(self) -> None:
        assert ProductionConfig.TESTING is False

    @pytest.mark.unit
    def test_inherits_from_default_config(self) -> None:
        assert issubclass(ProductionConfig, DefaultConfig)

    @pytest.mark.unit
    def test_sqlalchemy_track_modifications_is_false(self) -> None:
        assert ProductionConfig.SQLALCHEMY_TRACK_MODIFICATIONS is False

    @pytest.mark.unit
    def test_database_uri_uses_mysql_driver(self) -> None:
        assert ProductionConfig.SQLALCHEMY_DATABASE_URI.startswith("mysql+pymysql://")
