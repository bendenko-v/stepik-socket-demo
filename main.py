import contextlib

import uvicorn

from components import app
from src.events import register_events

register_events()

if __name__ == "__main__":
    with contextlib.suppress(KeyboardInterrupt):
        uvicorn.run(app, host="127.0.0.1", port=5000)
