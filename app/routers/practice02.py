from fastapi import APIRouter

from app.services.redis_service import StringService


router = APIRouter(prefix="/pr2", tags=["Счетчики и TTL"])


strings = StringService()


@router.get("/counter-create")
def counter_create():
    strings.set("page:home:views", "0")
    value = strings.get("page:home:views")
    return {
        "команда": "SET page:home:views 0",
        "ответ": "OK",
        "текущее_значение": value,
    }

@router.get("/counter-incr")
def counter_incr():
    if not strings.exists("page:home:views"):
        strings.set("page:home:views", "0")

    results = []
    for _ in range(10):
        val = strings.incr("page:home:views")
        results.append(val)

    return {
        "команда": "INCR page:home:views (×10)",
        "значения_после_каждого_INCR": results,
        "итоговое_значение": strings.get("page:home:views"),
    }

@router.get("/likes")
def likes():
    strings.delete("post:10:likes") 
    strings.incr("post:10:likes") #Если ключа нет, то incr автоматически 
    #создает ключ и присваивает ему значение "0" и увеличивает на единицу
    strings.incr("post:10:likes")
    strings.incr("post:10:likes")
    value = strings.get("post:10:likes")

    return {
        "команда": "INCR post:10:likes (×3)",
        "ответ": value,
        "пояснение": "3 лайка на посте #10",
    }

@router.get("/session-ttl")
def session_ttl():
    strings.set("session:user1", "token123", ex=60)
    ttl = strings.ttl("session:user1")
    value = strings.get("session:user1")

    return {
        "команда": 'SET session:user1 "token123" EX 60',
        "значение": value,
        "ttl_секунд": ttl,
        "пояснение": f"Ключ удалится через {ttl} секунд",
    }
