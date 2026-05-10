import pytest

from src.constants.vars import (
    APP_VIEW_ROUTE_NAME,
    BLUEPRINT_NOTES_PATH,
    NOTES_BLUEPRINT_ROUTE_NAME,
    TEMPLATE_HOME_NAME,
    VERSION_BLUEPRINTS,
    VERSION_VIEWS,
    VIEW_APP_PATH,
)


class TestVersionConstants:
    @pytest.mark.unit
    def test_version_views_is_string(self) -> None:
        assert isinstance(VERSION_VIEWS, str)

    @pytest.mark.unit
    def test_version_blueprints_is_string(self) -> None:
        assert isinstance(VERSION_BLUEPRINTS, str)


class TestRouteNameConstants:
    @pytest.mark.unit
    def test_notes_blueprint_route_name(self) -> None:
        assert NOTES_BLUEPRINT_ROUTE_NAME == "notes"

    @pytest.mark.unit
    def test_app_view_route_name(self) -> None:
        assert APP_VIEW_ROUTE_NAME == "app_view"


class TestPathConstants:
    @pytest.mark.unit
    def test_blueprint_notes_path_starts_with_api(self) -> None:
        assert BLUEPRINT_NOTES_PATH.startswith("/api/")

    @pytest.mark.unit
    def test_blueprint_notes_path_contains_notes(self) -> None:
        assert "notes" in BLUEPRINT_NOTES_PATH

    @pytest.mark.unit
    def test_view_app_path_starts_with_views(self) -> None:
        assert VIEW_APP_PATH.startswith("/views/")

    @pytest.mark.unit
    def test_template_home_name_ends_with_html(self) -> None:
        assert TEMPLATE_HOME_NAME.endswith(".html")
