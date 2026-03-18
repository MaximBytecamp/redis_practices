from fastapi import APIRouter

from app.services.redis_service import SortedSetService, StringService

router = APIRouter(prefix="/pr6", tags=["Практика 6. Sorted Set — рейтинги"])

zsets = SortedSetService()
strings = StringService()

@router.get("/create-leaderboard")
def create_leaderboard():
    strings.delete("leaderboard")
    zsets.zadd("leaderboard", {"Ivan": 1200, "Maxim": 1500, "Olga": 1800})

    top = zsets.zrange("leaderboard", 0, -1, withscores=True)

    return {
        "команды": [
            "ZADD leaderboard 1200 Ivan",
            "ZADD leaderboard 1500 Maxim",
            "ZADD leaderboard 1800 Olga",
        ],
        "рейтинг_по_возрастанию": [
            {"игрок": name, "очки": int(score)} for name, score in top
        ],
    }

@router.get("/top-players")
def top_players():
    if not strings.exists("leaderboard"):
        zsets.zadd("leaderboard", {"Ivan": 1200, "Maxim": 1500, "Olga": 1800})

    top = zsets.zrevrange("leaderboard", 0, -1, withscores=True)

    return {
        "команда": "ZREVRANGE leaderboard 0 -1 WITHSCORES",
        "топ_игроков": [
            {"место": i + 1, "игрок": name, "очки": int(score)}
            for i, (name, score) in enumerate(top)
        ],
    }

@router.get("/player-score")
def player_score():
    if not strings.exists("leaderboard"):
        zsets.zadd("leaderboard", {"Ivan": 1200, "Maxim": 1500, "Olga": 1800})

    score = zsets.zscore("leaderboard", "Maxim")
    rank = zsets.zrank("leaderboard", "Maxim")

    return {
        "игрок": "Maxim",
        "очки": int(score) if score else None,
        "позиция_снизу": rank,
        "пояснение": f"Maxim на {rank + 1}-м месте снизу (0 = последнее место)",
    }
