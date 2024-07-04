from components import sio


def register_events() -> None:
    """Register Socket.IO events."""
    sio.on("connect", connect)
    sio.on("disconnect", disconnect_user)
    sio.on("join", join)
    sio.on("message", message)


async def connect(sid, data):
    await sio.emit("welcome", {"code": 7007}, to=sid)


async def disconnect_user(sid):
    pass


async def join(sid, data):
    await sio.emit("status_update", {"status": "joined", "code": 8888}, to=sid)


async def message(sid, data):
    body = data.get("body")
    if not body:
        await sio.emit("error", {"message": "Не хватает ключа 'body'", "code": 1984}, to=sid)
        return

    if body == "Привет!":
        await sio.emit("message", {"message": "Привет от сервера!", "code": 1234}, to=sid)
        return

    await sio.emit("message", {"error": "Неверный текст сообщения, ожидается 'Привет!'"}, to=sid)
