from fastapi import APIRouter

from app.services.redis_service import SetService, StringService

router = APIRouter(prefix="/pr5", tags=["Практика 5. Set — множества"])

sets = SetService()
strings = StringService()

@router.get("/create-tournament")
def create_tournament():
    strings.delete("tournament:1")
    sets.sadd("tournament:1", "Ivan", "Maxim", "Olga")

    # Попробуем добавить дубль
    added = sets.sadd("tournament:1", "Ivan")
    members = sets.smembers("tournament:1")

    return {
        "команды": [
            "SADD tournament:1 Ivan",
            "SADD tournament:1 Maxim",
            "SADD tournament:1 Olga",
        ],
        "участники": list(members),
        "повторное_добавление_Ivan": added,
        "пояснение": "Добавлено 0 — Ivan уже в множестве (дубли не добавляются)",
    }


@router.get("/check-members")
def check_members():
    if not strings.exists("tournament:1"):
        sets.sadd("tournament:1", "Ivan", "Maxim", "Olga")

    members = sets.smembers("tournament:1")
    is_ivan = sets.sismember("tournament:1", "Ivan")
    is_alex = sets.sismember("tournament:1", "Alex")

    return {
        "участники": list(members),
        "Ivan_участвует": bool(is_ivan),
        "Alex_участвует": bool(is_alex),
    }


@router.get("/remove-member")
def remove_member():
    if not strings.exists("tournament:1"):
        sets.sadd("tournament:1", "Ivan", "Maxim", "Olga")

    sets.srem("tournament:1", "Ivan")
    members = sets.smembers("tournament:1")

    return {
        "команда": "SREM tournament:1 Ivan",
        "участники_после": list(members),
        "пояснение": "Ivan удалён из турнира",
    }