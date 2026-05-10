from collections.abc import Generator

import pytest
from flask import Flask
from flask.testing import FlaskClient

from src import create_app
from src.configs.sql_alchemy_config import db


@pytest.fixture(scope="session")
def app() -> Generator[Flask, None, None]:
    flask_app: Flask = create_app("testing")
    with flask_app.app_context():
        db.create_all()
    yield flask_app
    with flask_app.app_context():
        db.session.remove()
        db.drop_all()


@pytest.fixture(scope="function")
def client(app: Flask) -> FlaskClient:
    return app.test_client()


@pytest.fixture(scope="function")
def db_session(app: Flask) -> Generator[None, None, None]:
    with app.app_context():
        yield
        db.session.rollback()
        for table in reversed(db.metadata.sorted_tables):
            db.session.execute(table.delete())
        db.session.commit()
