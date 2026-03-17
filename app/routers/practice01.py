from fastapi import APIRouter

from app.services.redis_service import StringService 


router = APIRouter(prefix="/pr1", tags=["CLI. Базовые команды"])

strings = StringService()

@router.get("/ping")
def ping():
    result = strings.ping()
    return {"command": "PING", "res": "PONG" if result else "Ошибка"}


@router.get("/set-get")
def set_get():
    strings.set("name", "Maxim")
    value = strings.get("name")

    return {
        "step1": {"comm": "SET name Maxim", "output": "OK"},
        "step2": {"comm": "GET name", "output": value}
    }

@router.get("/del-exists")
def del_exists():
    if not strings.exists("name"):
        strings.set("name", "Ivan")

    strings.delete("name")
    exists = strings.exists("name")

    return {"res": exists}



    