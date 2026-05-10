from livereload import Server

from src import create_app
from src.utils.helpers import get_watch_patterns

app = create_app("development")

if __name__ == "__main__":
    server = Server(app.wsgi_app)

    for pattern in get_watch_patterns():
        server.watch(pattern)

    server.serve(
        host=app.config["HOST"],
        port=int(app.config["PORT"]),
        liveport=35729,
    )
