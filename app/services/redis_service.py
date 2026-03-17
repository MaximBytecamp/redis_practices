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

