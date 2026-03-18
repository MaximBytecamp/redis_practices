import time 
from app.core.redis import get_redis 

class StringService:
    @staticmethod
    def ping() -> bool:
        return get_redis().ping()
    

    @staticmethod
    def set(key: str, value: str, ex: int | None = None) -> None: 
        get_redis().set(key, value, ex=ex)

    @staticmethod
    def get(key: str) -> str | None:
        return get_redis().get(key)
    
    @staticmethod
    def delete(key: str) -> int:
        return get_redis().delete(key)

    @staticmethod
    def exists(key: str) -> int:
        return get_redis().exists(key)
    
    @staticmethod
    def incr(key: str) -> int:
        return get_redis().incr(key)

    @staticmethod
    def ttl(key: str) -> int:
        return get_redis().ttl(key)


class HashService:
    @staticmethod
    def hset(key: str, mapping: dict | None = None, field: str | None = None, value: str | None = None) -> None:
        r = get_redis()
        if mapping:
            r.hset(key, mapping=mapping)
        elif field and value is not None:
            r.hset(key, field, value)

    @staticmethod
    def hgetall(key: str) -> dict:
        return get_redis().hgetall(key)
    

    @staticmethod
    def hget(key: str, field: str) -> str | None:
        return get_redis().hget(key, field)
    
    @staticmethod
    def hdel(key: str, field: str) -> int:
        return get_redis().hdel(key, field)

    @staticmethod
    def hincrby(key: str, field: str, amount: int) -> int:
        return get_redis().hincrby(key, field, amount)
    


class ListService:
    """Работа со списками Redis (List)."""

    @staticmethod
    def rpush(key: str, *values: str) -> int:
        return get_redis().rpush(key, *values)

    @staticmethod
    def lpop(key: str) -> str | None:
        return get_redis().lpop(key)

    @staticmethod
    def lrange(key: str, start: int = 0, end: int = -1) -> list:
        return get_redis().lrange(key, start, end)

    @staticmethod
    def llen(key: str) -> int:
        return get_redis().llen(key)


class SetService:
    """Работа с множествами Redis (Set)."""

    @staticmethod
    def sadd(key: str, *members: str) -> int:
        return get_redis().sadd(key, *members)

    @staticmethod
    def smembers(key: str) -> set:
        return get_redis().smembers(key)

    @staticmethod
    def srem(key: str, *members: str) -> int:
        return get_redis().srem(key, *members)

    @staticmethod
    def sismember(key: str, member: str) -> bool:
        return get_redis().sismember(key, member)

    @staticmethod
    def scard(key: str) -> int:
        return get_redis().scard(key)
    
class SortedSetService:
    """Работа с отсортированными множествами Redis (Sorted Set)."""

    @staticmethod
    def zadd(key: str, mapping: dict) -> int:
        return get_redis().zadd(key, mapping)

    @staticmethod
    def zrange(key: str, start: int = 0, end: int = -1, withscores: bool = False) -> list:
        return get_redis().zrange(key, start, end, withscores=withscores)

    @staticmethod
    def zrevrange(key: str, start: int = 0, end: int = -1, withscores: bool = False) -> list:
        return get_redis().zrevrange(key, start, end, withscores=withscores)

    @staticmethod
    def zscore(key: str, member: str) -> float | None:
        return get_redis().zscore(key, member)

    @staticmethod
    def zrank(key: str, member: str) -> int | None:
        return get_redis().zrank(key, member)

    @staticmethod
    def zrem(key: str, *members: str) -> int:
        return get_redis().zrem(key, *members)

    @staticmethod
    def zincrby(key: str, amount: float, member: str) -> float:
        return get_redis().zincrby(key, amount, member)