import pytest

from src.constants.paths import (
    CSS_FILES_PATH,
    JS_FILES_PATH,
    RENDER_TEMPLATE_HOME_PATH,
    SRC_PATH,
)


class TestRenderTemplatePath:
    @pytest.mark.unit
    def test_render_template_home_path_is_string(self) -> None:
        assert isinstance(RENDER_TEMPLATE_HOME_PATH, str)

    @pytest.mark.unit
    def test_render_template_home_path_ends_with_home_html(self) -> None:
        assert RENDER_TEMPLATE_HOME_PATH.endswith("home.html")

    @pytest.mark.unit
    def test_render_template_home_path_contains_app(self) -> None:
        assert "app" in RENDER_TEMPLATE_HOME_PATH


class TestStaticPaths:
    @pytest.mark.unit
    def test_src_path_is_string(self) -> None:
        assert isinstance(SRC_PATH, str)

    @pytest.mark.unit
    def test_css_files_path_contains_css(self) -> None:
        assert "css" in CSS_FILES_PATH.lower()

    @pytest.mark.unit
    def test_js_files_path_contains_js(self) -> None:
        assert "js" in JS_FILES_PATH.lower()
