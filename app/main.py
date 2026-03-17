from fastapi import FastAPI

from app.routers import practice01


app = FastAPI(
    title = "Практика по всем структурам данных в Redis",
    description=(
        "Каждый раздел = отдельная практическая работа.\n\n"
        "Выполняйте задания **по порядку** сверху вниз.\n\n"
        "Перед новой практикой можно очистить базу: `DELETE /utils/clear`"
    )
)

app.include_router(practice01.router)