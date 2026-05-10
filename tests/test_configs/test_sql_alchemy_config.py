import pytest
from flask_sqlalchemy import SQLAlchemy

from src.configs.sql_alchemy_config import db


class TestSQLAlchemyConfig:
    @pytest.mark.unit
    def test_db_is_sqlalchemy_instance(self) -> None:
        assert isinstance(db, SQLAlchemy)
