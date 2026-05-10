from typing import Any

import pytest
from flask import Flask

from src.utils.helpers import get_context_by_key, get_extra_files, get_watch_patterns


class TestGetContextByKey:
    @pytest.mark.unit
    def test_home_key_returns_current_route(self, app: Flask) -> None:
        context: dict[str, Any] = get_context_by_key(app=app, key="home")
        assert context["current_route"] == "Home"

    @pytest.mark.unit
    def test_home_key_returns_home_view(self, app: Flask) -> None:
        context: dict[str, Any] = get_context_by_key(app=app, key="home")
        assert context["home_view"] == app.config["HOME_VIEW"]

    @pytest.mark.unit
    def test_home_key_merges_extra_kwargs(self, app: Flask) -> None:
        notes: list[str] = []
        context: dict[str, Any] = get_context_by_key(app=app, key="home", notes=notes)
        assert "notes" in context
        assert context["notes"] is notes

    @pytest.mark.unit
    def test_unknown_key_returns_only_extra(self, app: Flask) -> None:
        context: dict[str, Any] = get_context_by_key(app=app, key="unknown", foo="bar")
        assert context == {"foo": "bar"}

    @pytest.mark.unit
    def test_unknown_key_returns_empty_dict_with_no_extra(self, app: Flask) -> None:
        context: dict[str, Any] = get_context_by_key(app=app, key="unknown")
        assert context == {}

    @pytest.mark.unit
    def test_extra_kwargs_override_base_for_same_key(self, app: Flask) -> None:
        context: dict[str, Any] = get_context_by_key(app=app, key="home", current_route="Custom")
        assert context["current_route"] == "Custom"


class TestGetWatchPatterns:
    @pytest.mark.unit
    def test_returns_list(self) -> None:
        result: list[str] = get_watch_patterns()
        assert isinstance(result, list)

    @pytest.mark.unit
    def test_returns_eight_patterns(self) -> None:
        result: list[str] = get_watch_patterns()
        assert len(result) == 8

    @pytest.mark.unit
    def test_all_elements_are_strings(self) -> None:
        result: list[str] = get_watch_patterns()
        assert all(isinstance(p, str) for p in result)


class TestGetExtraFiles:
    @pytest.mark.unit
    def test_returns_list(self) -> None:
        result: list[str] = get_extra_files()
        assert isinstance(result, list)

    @pytest.mark.unit
    def test_all_elements_are_strings(self) -> None:
        result: list[str] = get_extra_files()
        assert all(isinstance(f, str) for f in result)
