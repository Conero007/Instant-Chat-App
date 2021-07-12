import os
from website import create_app


socketio, app = create_app()


if __name__ == "__main__":
    host = '127.0.0.1'
    port = int(os.environ.get("PORT", 5000))
    socketio.run(app, host=host, port=port, debug=True)
