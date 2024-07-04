import socketio
from fastapi import FastAPI

from src.api.routes import router

fast_app = FastAPI()

fast_app.include_router(router)

sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins="*")
app = socketio.ASGIApp(sio, other_asgi_app=fast_app)
