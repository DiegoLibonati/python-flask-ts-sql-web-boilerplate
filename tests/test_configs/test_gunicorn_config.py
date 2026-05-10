import multiprocessing

import pytest

import src.configs.gunicorn_config as gunicorn_config


class TestGunicornConfigBind:
    @pytest.mark.unit
    def test_bind_is_string(self) -> None:
        assert isinstance(gunicorn_config.bind, str)

    @pytest.mark.unit
    def test_bind_contains_port(self) -> None:
        assert ":" in gunicorn_config.bind

    @pytest.mark.unit
    def test_bind_port_is_numeric(self) -> None:
        port_str: str = gunicorn_config.bind.split(":")[-1]
        assert port_str.isdigit()


class TestGunicornConfigWorkers:
    @pytest.mark.unit
    def test_workers_is_int(self) -> None:
        assert isinstance(gunicorn_config.workers, int)

    @pytest.mark.unit
    def test_workers_is_positive(self) -> None:
        assert gunicorn_config.workers > 0

    @pytest.mark.unit
    def test_workers_formula(self) -> None:
        expected: int = multiprocessing.cpu_count() * 2 + 1
        assert gunicorn_config.workers == expected

    @pytest.mark.unit
    def test_threads_is_int(self) -> None:
        assert isinstance(gunicorn_config.threads, int)

    @pytest.mark.unit
    def test_threads_is_positive(self) -> None:
        assert gunicorn_config.threads > 0


class TestGunicornConfigTimeouts:
    @pytest.mark.unit
    def test_timeout_is_int(self) -> None:
        assert isinstance(gunicorn_config.timeout, int)

    @pytest.mark.unit
    def test_timeout_is_positive(self) -> None:
        assert gunicorn_config.timeout > 0

    @pytest.mark.unit
    def test_graceful_timeout_is_int(self) -> None:
        assert isinstance(gunicorn_config.graceful_timeout, int)

    @pytest.mark.unit
    def test_graceful_timeout_is_positive(self) -> None:
        assert gunicorn_config.graceful_timeout > 0


class TestGunicornConfigLogging:
    @pytest.mark.unit
    def test_loglevel_is_string(self) -> None:
        assert isinstance(gunicorn_config.loglevel, str)

    @pytest.mark.unit
    def test_loglevel_is_valid(self) -> None:
        valid_levels: list[str] = ["debug", "info", "warning", "error", "critical"]
        assert gunicorn_config.loglevel in valid_levels

    @pytest.mark.unit
    def test_accesslog_is_string(self) -> None:
        assert isinstance(gunicorn_config.accesslog, str)

    @pytest.mark.unit
    def test_errorlog_is_string(self) -> None:
        assert isinstance(gunicorn_config.errorlog, str)

    @pytest.mark.unit
    def test_proc_name_is_string(self) -> None:
        assert isinstance(gunicorn_config.proc_name, str)
