from fastapi import APIRouter, HTTPException, Request, status
from fastapi.responses import JSONResponse

router = APIRouter()


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
