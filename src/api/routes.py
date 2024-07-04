from io import BytesIO

from fastapi import APIRouter, HTTPException, Query, Request, status
from fastapi.responses import HTMLResponse, JSONResponse, StreamingResponse
from fastapi.templating import Jinja2Templates

from src.utils import generate_image

router = APIRouter()

templates = Jinja2Templates(directory="src/templates")


@router.get("/")
async def index():
    return JSONResponse(status_code=status.HTTP_200_OK, content={"status": "ok", "code": 2002})


@router.post("/")
async def create(request: Request):
    if request.headers.get("content-type") != "application/json":
        raise HTTPException(
            status_code=400,
            detail={"status": "error", "error": "Неверный content-type, ожидается тип 'application/json'"},
        )

    message = await request.json()

    if message.get("message"):
        return JSONResponse(status_code=status.HTTP_200_OK, content={"status": "ok", "code": 4321})

    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"status": "error", "error": "Отсутствует ключ 'message'"},
    )


@router.get("/gen_image", name="gen_image")
async def gen_image(name: str = Query(default="Unknown"), score: str = Query(default="0")):
    img = generate_image(name, score)

    img_io = BytesIO()
    img.save(img_io, "PNG")
    img_io.seek(0)

    return StreamingResponse(img_io, media_type="image/png")


@router.get("/share", response_class=HTMLResponse)
async def share(request: Request, name: str = Query(default="Unknown"), score: str = Query(default="0")):
    return templates.TemplateResponse("share.html", {"request": request, "name": name, "score": score})
