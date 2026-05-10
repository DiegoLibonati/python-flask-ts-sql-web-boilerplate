import glob
from typing import Any

from flask import Flask

from src.constants.paths import (
    APP_FILES_PATH,
    APP_FILES_PATH_2,
    CSS_FILES_PATH,
    CSS_FILES_PATH_2,
    GENERAL_FILES_PATH,
    GENERAL_FILES_PATH_2,
    JS_FILES_PATH,
    JS_FILES_PATH_2,
)


def get_watch_patterns() -> list[str]:
    return [
        GENERAL_FILES_PATH,
        GENERAL_FILES_PATH_2,
        APP_FILES_PATH,
        APP_FILES_PATH_2,
        JS_FILES_PATH,
        JS_FILES_PATH_2,
        CSS_FILES_PATH,
        CSS_FILES_PATH_2,
    ]


def get_extra_files() -> list[str]:
    extra_files = []
    for pattern in get_watch_patterns():
        extra_files.extend(glob.glob(pattern, recursive=True))
    return extra_files


def get_context_by_key(app: Flask, key: str, **extra: Any) -> dict[str, Any]:
    base: dict[str, Any] = {
        "home": {
            "current_route": "Home",
            "home_view": app.config["HOME_VIEW"],
        },
    }.get(key, {})

    return {**base, **extra}
