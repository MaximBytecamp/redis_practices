from fastapi import APIRouter

from app.services.redis_service import HashService, StringService

router = APIRouter(prefix="/pr3", tags=["Практика 3. Hash — объекты"])

hashes = HashService()
strings = StringService()


@router.get("/create-profile")
def create_profile():
    hashes.hset("user:1", mapping={"name": "Ivan", "age": "21", "city": "Moscow"})
    data = hashes.hgetall("user:1")

    return {
        "команда": "HSET user:1 name Ivan age 21 city Moscow",
        "ответ": "OK",
        "профиль": data,
    }


@router.get("/get-field")
def get_field():
    if not strings.exists("user:1"):
        hashes.hset("user:1", mapping={"name": "Ivan", "age": "21", "city": "Moscow"})

    name = hashes.hget("user:1", "name")
    all_fields = hashes.hgetall("user:1")

    return {
        "шаг_1": {"команда": "HGET user:1 name", "ответ": name},
        "шаг_2": {"команда": "HGETALL user:1", "ответ": all_fields},
    }

@router.get("/update-field")
def update_field():
    if not strings.exists("user:1"):
        hashes.hset("user:1", mapping={"name": "Ivan", "age": "21", "city": "Moscow"})

    hashes.hset("user:1", field="age", value="22")
    data = hashes.hgetall("user:1")

    return {
        "команда": "HSET user:1 age 22",
        "профиль_после": data,
        "пояснение": "Возраст изменился на 22, остальное осталось",
    }


@router.get("/delete-field")
def delete_field():
    if not strings.exists("user:1"):
        hashes.hset("user:1", mapping={"name": "Ivan", "age": "22", "city": "Moscow"})

    hashes.hdel("user:1", "city")
    data = hashes.hgetall("user:1")

    return {
        "команда": "HDEL user:1 city",
        "профиль_после": data,
        "пояснение": "Поле city удалено",
    }
