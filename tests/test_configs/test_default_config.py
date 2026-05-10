import pytest

from src.configs.default_config import DefaultConfig


class TestDefaultConfigFlags:
    @pytest.mark.unit
    def test_debug_is_false(self) -> None:
        assert DefaultConfig.DEBUG is False

    @pytest.mark.unit
    def test_testing_is_false(self) -> None:
        assert DefaultConfig.TESTING is False

    @pytest.mark.unit
    def test_sqlalchemy_track_modifications_is_false(self) -> None:
        assert DefaultConfig.SQLALCHEMY_TRACK_MODIFICATIONS is False


class TestDefaultConfigDatabase:
    @pytest.mark.unit
    def test_database_uri_uses_mysql_pymysql_driver(self) -> None:
        assert DefaultConfig.SQLALCHEMY_DATABASE_URI.startswith("mysql+pymysql://")

    @pytest.mark.unit
    def test_database_uri_contains_host(self) -> None:
        assert DefaultConfig.MYSQL_HOST in DefaultConfig.SQLALCHEMY_DATABASE_URI

    @pytest.mark.unit
    def test_database_uri_contains_db_name(self) -> None:
        assert DefaultConfig.MYSQL_DB_NAME in DefaultConfig.SQLALCHEMY_DATABASE_URI

    @pytest.mark.unit
    def test_mysql_port_defaults_to_int_or_string(self) -> None:
        assert DefaultConfig.MYSQL_PORT is not None


class TestDefaultConfigServer:
    @pytest.mark.unit
    def test_host_is_string(self) -> None:
        assert isinstance(DefaultConfig.HOST, str)

    @pytest.mark.unit
    def test_port_is_int(self) -> None:
        assert isinstance(DefaultConfig.PORT, int)

    @pytest.mark.unit
    def test_secret_key_is_string(self) -> None:
        assert isinstance(DefaultConfig.SECRET_KEY, str)


class TestDefaultConfigRoutes:
    @pytest.mark.unit
    def test_get_all_notes_route_references_notes_blueprint(self) -> None:
        assert "notes" in DefaultConfig.GET_ALL_NOTES_ROUTE

    @pytest.mark.unit
    def test_home_view_references_app_view(self) -> None:
        assert "app_view" in DefaultConfig.HOME_VIEW

    @pytest.mark.unit
    def test_blueprint_paths_start_with_api(self) -> None:
        assert DefaultConfig.GET_ALL_NOTES_ROUTE_PATH.startswith("/api/")
