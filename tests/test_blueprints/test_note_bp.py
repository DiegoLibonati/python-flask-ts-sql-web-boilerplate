import pytest
from flask import Flask


class TestNoteBlueprintRegistration:
    @pytest.mark.unit
    def test_notes_blueprint_is_registered(self, app: Flask) -> None:
        assert "notes" in app.blueprints

    @pytest.mark.unit
    def test_app_view_blueprint_is_registered(self, app: Flask) -> None:
        assert "app_view" in app.blueprints


class TestNoteBlueprintRoutes:
    @pytest.mark.unit
    def test_alive_route_exists(self, app: Flask) -> None:
        rules: list[str] = [str(rule) for rule in app.url_map.iter_rules()]
        assert "/api/v1/notes/alive" in rules

    @pytest.mark.unit
    def test_notes_root_route_exists(self, app: Flask) -> None:
        rules: list[str] = [str(rule) for rule in app.url_map.iter_rules()]
        assert "/api/v1/notes/" in rules

    @pytest.mark.unit
    def test_notes_id_route_exists(self, app: Flask) -> None:
        rules: list[str] = [str(rule) for rule in app.url_map.iter_rules()]
        assert "/api/v1/notes/<id>" in rules

    @pytest.mark.unit
    def test_alive_route_allows_get(self, app: Flask) -> None:
        rule = next(r for r in app.url_map.iter_rules() if str(r) == "/api/v1/notes/alive")
        assert "GET" in rule.methods

    @pytest.mark.unit
    def test_notes_root_route_allows_get_and_post(self, app: Flask) -> None:
        methods: set[str] = set()
        for rule in app.url_map.iter_rules():
            if str(rule) == "/api/v1/notes/":
                methods.update(rule.methods)
        assert "GET" in methods
        assert "POST" in methods

    @pytest.mark.unit
    def test_notes_id_route_allows_delete_and_patch(self, app: Flask) -> None:
        methods: set[str] = set()
        for rule in app.url_map.iter_rules():
            if str(rule) == "/api/v1/notes/<id>":
                methods.update(rule.methods)
        assert "DELETE" in methods
        assert "PATCH" in methods
