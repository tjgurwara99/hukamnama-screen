from hukamnama.extensions import socketio


@socketio.on("connect")
def handle_connect():
    pass
