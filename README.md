# Python Flask Ts SQL Web Boilerplate

## Educational Purpose

This project was created primarily for **educational and learning purposes**.
While it is well-structured and could technically be used in production, it is **not intended for commercialization**.
The main goal is to explore and demonstrate best practices, patterns, and technologies in software development.

## Description

**Python Flask Ts SQL Web Boilerplate** is a production-ready boilerplate for building full-stack web applications with **Flask**, **SQLAlchemy**, and **TypeScript**, designed to eliminate the repetitive setup that comes with every new MVC web project.

**What it is:** A starting point — not a framework — for developers who want to spin up a Flask + MySQL + TypeScript web app without rebuilding the same infrastructure from scratch each time. Every layer, pattern, and tooling choice is already wired together and working.

**The problem it solves:** Starting a Flask MVC project from zero means making the same decisions repeatedly: how to structure layers, how to handle errors globally, how to connect to MySQL through SQLAlchemy, how to write and compile TypeScript without a JS framework, how to configure environments, how to set up Docker, linting, migrations, and tests for both backend and frontend. This boilerplate makes all those decisions once, so you can focus on building the actual product.

**What it includes:**
- **Layered MVC architecture** enforced by convention: Blueprint → Controller → Service → DAO → SQLAlchemy ORM. Each layer has a single responsibility and only talks to the one directly below it. A separate view layer handles Jinja2 template rendering.
- **SQLAlchemy 2.0** ORM with `Mapped[...]` and `mapped_column` syntax, backed by **MySQL** in Docker. Schema changes are managed through **Flask-Migrate** (Alembic under the hood).
- **Custom exception hierarchy** (`ValidationAPIError`, `NotFoundAPIError`, `ConflictAPIError`, `BusinessAPIError`, `InternalAPIError`) that produces consistent JSON error responses across the entire API. A `handle_exceptions` decorator automatically catches `SQLAlchemyError` and uncaught exceptions without polluting controller code with try/catch blocks.
- **TypeScript** frontend with no JS framework dependency — compiled with `tsc` and watched automatically in development. Tested with **Jest** and **Testing Library**.
- **Environment-based configuration** using a `DefaultConfig` base class extended by `DevelopmentConfig`, `TestingConfig`, and `ProductionConfig`, loaded dynamically by the app factory via `importlib`.
- **Docker** setup for development and production. The development compose includes the Flask app, MySQL, and **Adminer** for database inspection. Production uses **Gunicorn** as the WSGI server behind **Nginx** as a reverse proxy.
- **Ruff** for fast Python linting and formatting, enforced automatically via **pre-commit** hooks on every commit, alongside **pip-audit** for dependency vulnerability scanning.
- **pytest** configured with `pytest-env` and `pytest-cov`, organized to mirror the `src/` structure. A dedicated `test.docker-compose.yml` spins up a real MySQL container for integration tests — no mocked databases.
- **Jest** configured for TypeScript with `ts-jest`, `jest-environment-jsdom`, and **Testing Library** for DOM-level testing of frontend modules.

**How to use it:** Clone the repository, bring up the Docker environment, and replace the `note` resource (blueprint, controller, service, DAO, ORM model, view, constants) with your own domain logic. The architecture, tooling, error handling, migrations, and test setup are already in place — you only write what's unique to your application.

## Technologies used

The stack underpinning every layer described above:

Backend:

1. Python 3.11+
2. Flask 3.1
3. SQLAlchemy 2.0
4. Flask-Migrate (Alembic)
5. Jinja2

Frontend:

1. TypeScript 5.6
2. CSS3
3. HTML5

Deploy:

1. Docker
2. Gunicorn
3. Nginx

Database:

1. MySQL 8.0

## Libraries used

Exact pinned versions per requirements file — these are what gets installed when you follow [Getting Started](#getting-started).

#### Dependencies JS

```
No dependencies in package.json
```

#### devDependencies JS

```
"@eslint/js": "^9.39.2"
"@testing-library/dom": "^10.4.0"
"@testing-library/jest-dom": "^6.6.3"
"@testing-library/user-event": "^14.5.2"
"@types/jest": "^30.0.0"
"@types/node": "^22.0.0"
"chokidar-cli": "^3.0.0"
"eslint": "^9.39.2"
"eslint-config-prettier": "^10.1.8"
"eslint-plugin-prettier": "^5.5.5"
"globals": "^17.3.0"
"globby": "^15.0.0"
"husky": "^9.1.7"
"jest": "^30.3.0"
"jest-environment-jsdom": "^30.3.0"
"lint-staged": "^16.2.7"
"prettier": "^3.8.1"
"ts-jest": "^29.4.6"
"tsc-alias": "^1.8.16"
"typescript": "^5.6.3"
"typescript-eslint": "^8.54.0"
```

#### Flask requirements.txt

```
flask==3.1.3
flask-sqlalchemy==3.1.1
flask-migrate==4.1.0
werkzeug==3.1.8
gunicorn==23.0.0
pymysql==1.1.3
cryptography==48.0.0
```

#### Flask requirements.dev.txt

```
-r requirements.txt
livereload==2.7.0
pre-commit==4.3.0
pip-audit==2.7.3
ruff==0.11.12
```

#### Flask requirements.test.txt

```
pytest==8.4.2
pytest-env==1.1.5
pytest-cov==4.1.0
pytest-timeout==2.3.1
pytest-xdist==3.5.0
```

## Getting Started

With the stack and libraries above in mind, follow these steps to get a working dev environment.

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) — must be running before executing any compose command
- [Node.js](https://nodejs.org/) 22+ with npm or yarn — required to install frontend dependencies
- Python 3.11+ — only required if you want to run pre-commit, tests, or migrations outside Docker
- Git

### Setup

1. **Clone the repository:**

   ```sh
   git clone "repository link"
   cd python-flask-ts-sql-web-boilerplate
   ```

2. **Create the environment file** from the provided example and fill in the values (see [Env Keys](#env-keys) for what each variable does):

   ```sh
   cp .env.example .env        # macOS / Linux / Git Bash
   copy .env.example .env      # Windows CMD
   ```

3. **Install frontend dependencies** (required for the TypeScript watcher inside Docker):

   ```sh
   cd src/static/ts
   npm install
   # or
   yarn install
   ```

4. **Build the Docker image** from the project root:

   ```sh
   docker compose -f dev.docker-compose.yml build --no-cache
   ```

5. **Start the containers:**

   ```sh
   docker compose -f dev.docker-compose.yml up --force-recreate
   ```

Once running, the services are available at:

| Service | URL |
|---|---|
| Flask app | http://localhost:5050 |
| Adminer (DB UI) | http://localhost:8080 |

### Pre-Commit for Development

Pre-commit hooks (Ruff lint + format, pip-audit) run automatically on every `git commit`. Setup requires a local Python virtual environment because `pre-commit` is a Python package and is also the same env you'll use for [Testing](#testing) and [Migrations](#migrations).

1. **Create and activate the virtual environment** at the repository root:

   ```sh
   python -m venv venv
   venv\Scripts\activate          # Windows
   source venv/bin/activate       # Linux / macOS
   ```

2. **Install all Python dependencies:**

   ```sh
   pip install -r requirements.txt
   pip install -r requirements.dev.txt
   pip install -r requirements.test.txt
   ```

3. **Install the pre-commit hooks** declared in `.pre-commit-config.yaml`:

   ```sh
   pre-commit install
   ```

   From now on, every `git commit` will trigger the hooks. To run them manually against the entire repo:

   ```sh
   pre-commit run --all-files
   ```

## Env Keys

The variables loaded from `.env` (created in step 2 of [Setup](#setup)). Defaults provided in `.env.example` work out of the box for local Docker development; production deploys must override `SECRET_KEY` and the MySQL credentials.

| Key | Description |
|---|---|
| `HOST` | Network interface where Flask listens (`0.0.0.0` to accept all connections). |
| `PORT` | Port where the Flask app is exposed inside the container. |
| `SECRET_KEY` | Flask secret key used for session signing and CSRF protection. Use a long random string in production. |
| `MYSQL_ROOT_PASSWORD` | Root password for the MySQL service. Used internally by Docker for initialization only. |
| `MYSQL_HOST` | Hostname of the MySQL container in the Docker network (service name in Compose). |
| `MYSQL_PORT` | Port where MySQL listens inside the Docker network (`3306`). |
| `MYSQL_USER` | Non-root MySQL user that the Flask app uses to connect. |
| `MYSQL_PASSWORD` | Password for `MYSQL_USER`. |
| `MYSQL_DB_NAME` | Name of the MySQL database created automatically by the container. |

```sh
HOST="0.0.0.0"
PORT=5050
SECRET_KEY="secret_key"

MYSQL_ROOT_PASSWORD=root
MYSQL_HOST=boilerplate-db
MYSQL_PORT=3306
MYSQL_USER=boilerplate_user
MYSQL_PASSWORD=boilerplate_pass
MYSQL_DB_NAME=boilerplate_db
```

## Project Structure

Layout of the codebase you just cloned. Each top-level folder is explained in the glossary below the tree.

```
python-flask-ts-sql-web-boilerplate/
│
├── src/
│   ├── __init__.py                         # App factory: create_app(config_name)
│   │
│   ├── blueprints/                         # API route registration
│   │   ├── __init__.py
│   │   ├── routes.py                       # Registers all API blueprints
│   │   └── v1/
│   │       ├── __init__.py
│   │       └── note_bp.py                  # Blueprint for /api/v1/notes/ endpoints
│   │
│   ├── configs/                            # Environment-based configuration
│   │   ├── default_config.py               # Base config with shared defaults
│   │   ├── development_config.py           # Development overrides (DEBUG=True)
│   │   ├── production_config.py            # Production overrides
│   │   ├── testing_config.py               # Test config with SQLite in-memory DB
│   │   ├── gunicorn_config.py              # Gunicorn WSGI server settings
│   │   ├── logger_config.py                # App-wide logger setup
│   │   └── sql_alchemy_config.py           # SQLAlchemy db instance
│   │
│   ├── constants/                          # Application-wide constants
│   │   ├── __init__.py
│   │   ├── codes.py                        # Error/response codes
│   │   ├── messages.py                     # User-facing messages
│   │   ├── paths.py                        # URL path constants
│   │   └── vars.py                         # Misc. config variables
│   │
│   ├── controllers/                        # Parse request, call service, return response
│   │   ├── __init__.py
│   │   └── note_controller.py              # CRUD handlers for notes
│   │
│   ├── data_access/                        # Database access layer (DAOs)
│   │   ├── __init__.py
│   │   └── note_dao.py                     # SQLAlchemy queries for Note model
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── orm/                            # SQLAlchemy ORM models
│   │       ├── __init__.py
│   │       └── note.py                     # Note model (Mapped[...], mapped_column)
│   │
│   ├── services/                           # Business logic layer
│   │   ├── __init__.py
│   │   └── note_service.py                 # Note business rules, calls NoteDAO
│   │
│   ├── static/
│   │   ├── pbulic/                         # Public folder for statics
│   │   ├── css/                            # Component and global stylesheets
│   │   ├── js/                             # Compiled TypeScript output
│   │   └── ts/                             # TypeScript source code
│   │       ├── __tests__/                  # Jest tests + mocks
│   │       ├── components/                 # UI components
│   │       ├── helpers/                    # Utility functions
│   │       ├── services/                   # Frontend API service layer
│   │       ├── package.json
│   │       └── tsconfig.json
│   │
│   ├── templates/                          # Jinja2 HTML templates
│   │   └── v1/
│   │       ├── base.html                   # Base layout template
│   │       └── app/
│   │           └── home.html               # Main app view
│   │
│   ├── utils/                              # Shared utilities
│   │   ├── exceptions.py                   # Custom exception hierarchy (BaseAPIError, etc.)
│   │   ├── error_handler.py                # handle_exceptions decorator
│   │   └── helpers.py                      # General-purpose helpers
│   │
│   └── views/                              # HTML view routes (render_template)
│       ├── routes.py                       # Registers all view blueprints
│       └── v1/
│           └── app_view.py                 # Routes for /views/v1/app/
│
├── migrations/                             # Alembic migration scripts (Flask-Migrate)
│
├── tests/
│   ├── conftest.py                         # Shared fixtures: app, client, db_session
│   ├── test_blueprints/                    # Tests for API blueprint routes
│   ├── test_configs/                       # Tests for all config modules
│   ├── test_constants/                     # Tests for constants modules
│   ├── test_controllers/                   # Tests for controllers (mocked service)
│   ├── test_data_access/                   # Integration tests for DAOs (real SQLite)
│   ├── test_models/                        # Tests for ORM models
│   ├── test_services/                      # Unit tests for services (mocked DAO)
│   ├── test_utils/                         # Tests for exceptions and error handler
│   └── test_views/                         # Tests for HTML view routes
│
├── app.py                                  # Development entry point
├── dev.docker-compose.yml                  # Dev environment: Flask + MySQL + Adminer
├── prod.docker-compose.yml                 # Production environment: Gunicorn + Nginx + MySQL
├── test.docker-compose.yml                 # Isolated MySQL container for integration tests
├── Dockerfile.development
├── Dockerfile.production
├── nginx.conf                              # Nginx reverse proxy config
├── entrypoint.development.sh
├── entrypoint.production.sh
├── pyproject.toml                          # Ruff + pytest configuration
├── requirements.txt                        # Production dependencies
├── requirements.dev.txt                    # Dev dependencies (Ruff, pre-commit, pip-audit)
├── requirements.test.txt                   # Test dependencies (pytest, pytest-cov, etc.)
├── .env.example                            # Environment variable template
└── .pre-commit-config.yaml                 # Pre-commit hooks (Ruff, pip-audit)
```

1. **`src/__init__.py`** — App factory. Calls `create_app(config_name)`, loads config dynamically via `importlib`, initializes SQLAlchemy, Flask-Migrate, and registers API blueprints and view routes.
2. **`src/blueprints/`** — API route layer. Each resource has its own versioned blueprint (e.g., `note_bp.py` for `/api/v1/notes/`). Routes delegate directly to controllers.
3. **`src/configs/`** — Environment-based configuration. `DefaultConfig` is the base; `DevelopmentConfig`, `TestingConfig`, and `ProductionConfig` extend it. Loaded by name via `importlib` in the app factory.
4. **`src/constants/`** — Centralized constants for error codes, user-facing messages, URL paths, and variables. No logic here.
5. **`src/controllers/`** — Thin layer between routes and services. Parses the request, calls the appropriate service method, and returns a Flask response. No business logic.
6. **`src/data_access/`** — Data access objects (DAOs). All SQLAlchemy queries live here. Controllers and services never touch `db.session` directly.
7. **`src/models/orm/`** — SQLAlchemy 2.0 ORM models using `Mapped[...]` and `mapped_column`. Schema changes are managed through Flask-Migrate (Alembic).
8. **`src/services/`** — Business logic layer. Validates input, applies rules, and orchestrates DAO calls. Never touches `db.session` or Flask request/response objects.
9. **`src/static/ts/`** — TypeScript source code. Compiled to `src/static/js/` via `tsc`. No framework — DOM manipulation, fetch calls, and Jest tests only.
10. **`src/templates/`** — Jinja2 HTML templates. `base.html` defines the shared layout; page templates extend it. Rendered by view routes, not API routes.
11. **`src/utils/`** — Shared utilities. `exceptions.py` defines the custom exception hierarchy; `error_handler.py` provides the `@handle_exceptions` decorator that auto-wraps `SQLAlchemyError` and uncaught exceptions into consistent `InternalAPIError` responses.
12. **`src/views/`** — HTML rendering routes. Separate from API blueprints — these routes call services, render Jinja templates, and return full HTML pages.
13. **`tests/`** — Test suite mirroring `src/`. Unit tests mock DAOs and services; integration tests use a real SQLite in-memory database via the `db_session` fixture.
14. **`migrations/`** — Alembic migration scripts generated by `flask db migrate`. Run `flask db upgrade` to apply pending migrations.

## Architecture & Design Patterns

The folder layout above is not arbitrary — it enforces the following architectural rules and patterns.

### MVC (Model-View-Controller)

The application follows a strict MVC structure adapted for Flask:

- **Model** — SQLAlchemy ORM classes in `src/models/orm/`. Each model maps directly to a database table and exposes a `to_dict()` method for JSON serialization. No business logic lives in models.
- **View** — Two distinct view types coexist: API blueprints (`src/blueprints/`) return JSON; HTML views (`src/views/`) render Jinja2 templates. Both ultimately delegate to the same service layer.
- **Controller** — Functions in `src/controllers/` sit between routes and services. They parse the request, call the appropriate service method, and build the response. They contain no business logic and no direct database access.

### Layered Architecture

Every request flows strictly top-down through five layers. Each layer only talks to the one immediately below it — never skipping, never reaching up:

```
Blueprint (route)
    ↓
Controller (parse request → build response)
    ↓
Service (business logic + validation)
    ↓
DAO (database queries via db.session)
    ↓
ORM Model (SQLAlchemy table mapping)
```

This means:
- Controllers never import `db` or DAO classes.
- Services never import `db` or touch `request`/`jsonify`.
- DAOs never import services or contain business rules.
- Violations of these boundaries break the architecture.

### App Factory Pattern

`create_app(config_name)` in `src/__init__.py` constructs the Flask application on demand rather than at module import time. This enables:

- **Environment isolation** — different configs are loaded per environment (`development`, `testing`, `production`) simply by passing a different name.
- **Testability** — each test session can create a fresh app instance with `create_app("testing")`, preventing state leakage between test runs.
- **Dynamic config loading** — `importlib.import_module(f"src.configs.{config_name}_config")` resolves the config class at runtime with no hardcoded imports.

### Strategy Pattern — Environment Configuration

All config classes inherit from `DefaultConfig`, which defines every shared value with sensible defaults:

```
DefaultConfig (base)
├── DevelopmentConfig  → DEBUG=True
├── TestingConfig      → SQLite in-memory, TESTING=True
└── ProductionConfig   → DEBUG=False, hardened settings
```

Switching environments only requires passing a different `config_name` string to `create_app()`. No conditional logic exists inside the app — the config object itself carries the strategy.

### Data Access Object (DAO) Pattern

All SQLAlchemy interactions are isolated inside DAO classes (`src/data_access/`). Each DAO exposes static methods for querying and mutating a single resource:

```python
class NoteDAO:
    @staticmethod
    def query_all() -> list[Note]: ...

    @staticmethod
    def add(note: Note) -> Note: ...

    @staticmethod
    def update(note: Note, data: dict[str, Any]) -> None: ...
```

Mutation methods (`update`, `delete`) handle their own rollback on failure and re-raise the exception for the layer above to decide how to respond. This keeps `db.session` contained to a single layer and makes unit testing trivially easy — mock the DAO, never the session.

### Decorator Pattern — Exception Handling

`@handle_exceptions` (in `src/utils/error_handler.py`) is applied to every controller function. It intercepts exceptions at the boundary between the controller and the layers below, normalizing them into consistent API errors without polluting controller code with try/except blocks:

```
BaseAPIError subclass  →  re-raised as-is (already structured)
SQLAlchemyError        →  InternalAPIError(CODE_ERROR_DATABASE, 500)
Any other Exception    →  InternalAPIError(CODE_ERROR_GENERIC, 500)
```

The app factory registers a global `@app.errorhandler(BaseAPIError)` handler that calls `error.flask_response()` on any unhandled `BaseAPIError`, producing a consistent JSON body with `code`, `message`, and optional `payload`.

### Custom Exception Hierarchy

All domain errors derive from `BaseAPIError`, which carries an HTTP status code, a machine-readable `code` string, and a human-readable `message`. Subclasses fix the status code to a specific HTTP semantic:

| Exception | Status |
|---|---|
| `ValidationAPIError` | 400 |
| `NotFoundAPIError` | 404 |
| `ConflictAPIError` | 409 |
| `BusinessAPIError` | 422 |
| `InternalAPIError` | 500 |

Raising a typed exception anywhere in the stack is enough to produce the correct HTTP response — no conditional status-code logic needed in controllers.

### SQLAlchemy Event Listeners

The `Note` model uses `@event.listens_for` to normalize timezone data on load and refresh:

```python
@event.listens_for(Note, "load")
@event.listens_for(Note, "refresh")
def ensure_utc_timezone(note: Note, *_: Any) -> None:
    if note.created_at and note.created_at.tzinfo is None:
        note.created_at = note.created_at.replace(tzinfo=timezone.utc)
```

This handles the case where MySQL returns timezone-naive datetimes — the fix is applied transparently at the ORM layer rather than scattered across service or controller code.

## Migrations

Schema changes that follow from modifying ORM models are managed through **Flask-Migrate** (Alembic under the hood). Migration scripts live in `migrations/versions/`.

> Requires the local virtual environment from [Pre-Commit for Development](#pre-commit-for-development) and a running MySQL instance (or the dev Docker stack).

**Generate a new migration** after changing or adding a model in `src/models/orm/`:

```sh
flask db migrate -m "feat: add email column to User model"
```

Always review the generated script in `migrations/versions/` before applying — Alembic may miss certain changes (e.g., column type changes, constraints).

**Apply pending migrations:**

```sh
flask db upgrade
```

**Roll back the last migration:**

```sh
flask db downgrade
```

**Roll back to a specific revision:**

```sh
flask db downgrade <revision_id>
```

**Check current migration state:**

```sh
flask db current   # show applied revision
flask db history   # show full migration history
```

> In production, `flask db upgrade` runs automatically at container startup via `entrypoint.production.sh` — no manual step needed.

## Testing

With migrations applied and the app running, verify behavior end-to-end with the test suites for both backend and frontend.

### Backend

> Requires the local virtual environment from [Pre-Commit for Development](#pre-commit-for-development).

**Run all tests:**

```sh
python -m pytest
```

**Run with coverage report:**

```sh
python -m pytest --cov=src --cov-report=term-missing
```

**Run by marker:**

```sh
python -m pytest -m unit         # unit tests only (mocks, no DB)
python -m pytest -m integration  # integration tests only (real DB)
```

**Run integration tests with a real MySQL database:**

```sh
# 1. Start the test database
docker compose -f test.docker-compose.yml up -d

# 2. Run integration tests
python -m pytest -m integration

# 3. Tear down the test database
docker compose -f test.docker-compose.yml down -v
```

### Frontend

> Requires Node.js >=22.0.0.

1. Navigate to the `src/static/ts` directory:

```sh
cd src/static/ts
```

2. Install dependencies (skip if already installed):

```sh
npm install
```

3. Run the tests:

```sh
npm test                  # run all tests
npm run test:watch        # watch mode
npm run test:coverage     # with coverage report
```

## Security Audit

Beyond functional correctness, scan dependencies for known vulnerabilities before shipping.

### Backend

> Requires the local virtual environment from [Pre-Commit for Development](#pre-commit-for-development) (so `pip-audit` is installed).

```sh
pip-audit -r requirements.txt
```

### Frontend

```sh
cd src/static/ts
npm audit
```

## Build

When tests and audits pass, produce the distributable artifacts.

### Frontend (TypeScript → JavaScript)

The frontend has no JS framework. TypeScript sources in `src/static/ts/` are compiled to plain JavaScript in `src/static/js/` via `tsc` (with `tsc-alias` resolving path aliases and a post-processing step fixing relative imports).

```sh
cd src/static/ts
npm install        # skip if already installed
npm run build
```

The output in `src/static/js/` is what Flask serves in development and what Nginx serves directly in production.

### Docker images

Both stacks ship as Docker images.

**Development image** (Flask + auto-reload + TS watcher):

```sh
docker compose -f dev.docker-compose.yml build --no-cache
```

**Production image** — multi-stage `Dockerfile.production`: a `builder` stage compiles TypeScript and installs Python dependencies; a lean `runner` stage copies only the final artifacts and runs Gunicorn as a non-root user (`appuser`):

```sh
docker compose -f prod.docker-compose.yml build --no-cache
```

## Production

With [Tested](#testing), [Audited](#security-audit), and [Built](#build) artifacts ready, deploy the production stack: **Gunicorn** (WSGI server) behind **Nginx** (reverse proxy), with **MySQL 8.0** as the database — all orchestrated by Docker Compose.

### Architecture

```
Browser → Nginx (:8080) → Gunicorn (:5050) → Flask app
                ↓
        /static/ served directly by Nginx (no Python involved)
```

- **Nginx** handles TLS termination, static file serving with long-lived cache headers, gzip compression, and proxies all dynamic requests to Gunicorn.
- **Gunicorn** runs `cpu_count * 2 + 1` workers with 2 threads each. Config lives in `src/configs/gunicorn_config.py`.
- **MySQL** data is persisted in a named Docker volume (`db-data`). The container is never exposed to the host.

### Startup sequence

On every container start, `entrypoint.production.sh` runs automatically:

1. Waits until `flask db upgrade` succeeds (retries every 2s until the DB is ready).
2. Copies compiled static files to a shared Docker volume (consumed by Nginx).
3. Launches Gunicorn.

### Deploy

> Make sure the production image has been built — see [Build → Docker images](#docker-images).

1. **Configure production environment** — copy `.env.example` to `.env` and override the values for production (strong random `SECRET_KEY`, real DB credentials, the public host you'll bind to). Refer to [Env Keys](#env-keys) for the full list:

   ```sh
   cp .env.example .env
   ```

2. **Start all services:**

   ```sh
   docker compose -f prod.docker-compose.yml up -d
   ```

   Once running, the app is available at:

   | Service | URL |
   |---|---|
   | App (via Nginx) | http://localhost:8080 |

3. **Stop and tear down:**

   ```sh
   docker compose -f prod.docker-compose.yml down
   ```

   To also remove the database volume (destructive — deletes all data):

   ```sh
   docker compose -f prod.docker-compose.yml down -v
   ```

### Logs

```sh
docker compose -f prod.docker-compose.yml logs -f              # all services
docker compose -f prod.docker-compose.yml logs -f boilerplate  # Flask/Gunicorn only
docker compose -f prod.docker-compose.yml logs -f nginx        # Nginx only
```

## Endpoints API

Reference for the HTTP surface exposed by the deployed app.

### Views

---

- **Endpoint Name**: Home
- **Endpoint Method**: GET
- **Endpoint URL**: `/views/v1/app/home`
- **Description**: Renders the main HTML page. Fetches all notes and passes them to the Jinja2 template.
- **Response**: `200 OK` — HTML page

---

### Notes API

---

- **Endpoint Name**: Health Check
- **Endpoint Method**: GET
- **Endpoint URL**: `/api/v1/notes/alive`
- **Description**: Returns a liveness check confirming the notes blueprint is registered and responding.
- **Response**:

```json
{
    "message": "I am Alive!",
    "version_bp": "1.0.0",
    "name_bp": "Notes"
}
```

---

- **Endpoint Name**: Get All Notes
- **Endpoint Method**: GET
- **Endpoint URL**: `/api/v1/notes/`
- **Description**: Returns all notes ordered by creation date.
- **Response**:

```json
{
    "code": "SUCCESS_GET_ALL_NOTES",
    "message": "...",
    "data": [
        {
            "id": 1,
            "content": "note content",
            "created_at": "2026-05-10T12:00:00+00:00"
        }
    ]
}
```

---

- **Endpoint Name**: Create Note
- **Endpoint Method**: POST
- **Endpoint URL**: `/api/v1/notes/`
- **Description**: Creates a new note. Requires `Content-Type: application/json`.
- **Body**:

```json
{
    "content": "string"
}
```

- **Response** `201 Created`:

```json
{
    "code": "SUCCESS_ADD_NOTE",
    "message": "...",
    "redirect_to": "/views/v1/app/home"
}
```

- **Error** `400 Bad Request` — if `content` is missing or blank.

---

- **Endpoint Name**: Delete Note
- **Endpoint Method**: DELETE
- **Endpoint URL**: `/api/v1/notes/:id`
- **Description**: Deletes the note with the given `id`.
- **URL Params**: `id` — integer ID of the note.
- **Response** `200 OK`:

```json
{
    "code": "SUCCESS_DELETE_NOTE",
    "message": "...",
    "redirect_to": "/views/v1/app/home"
}
```

- **Errors**:
  - `400 Bad Request` — if `id` is not a valid integer.
  - `404 Not Found` — if no note with that `id` exists.

---

- **Endpoint Name**: Update Note
- **Endpoint Method**: PATCH
- **Endpoint URL**: `/api/v1/notes/:id`
- **Description**: Updates the content of the note with the given `id`. Requires `Content-Type: application/json`.
- **URL Params**: `id` — integer ID of the note.
- **Body**:

```json
{
    "content": "string"
}
```

- **Response** `200 OK`:

```json
{
    "code": "SUCCESS_EDIT_NOTE",
    "message": "...",
    "redirect_to": "/views/v1/app/home"
}
```

- **Errors**:
  - `400 Bad Request` — if `id` is not a valid integer, or `content` is missing or blank.
  - `404 Not Found` — if no note with that `id` exists.

---

## Known Issues

None at the moment.

## Version

```
APP VERSION: 0.0.1
README UPDATED: 10/05/2026
AUTHOR: Diego Libonati
```

## Portfolio Link

[`https://www.diegolibonati.com.ar/#/project/python-flask-ts-sql-web-boilerplate`](https://www.diegolibonati.com.ar/#/project/python-flask-ts-sql-web-boilerplate)
