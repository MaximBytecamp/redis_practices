from fastapi import APIRouter

from app.services.redis_service import ListService, StringService

router = APIRouter(prefix="/pr4", tags=["Практика 4. List — очереди"])

lists = ListService()
strings = StringService()

@router.get("/create-queue")
def create_queue():
    strings.delete("tasks")
    lists.rpush("tasks", "task1", "task2", "task3")
    tasks = lists.lrange("tasks")

    return {
        "команды": [
            "RPUSH tasks task1",
            "RPUSH tasks task2",
            "RPUSH tasks task3",
        ],
        "очередь": tasks,
        "размер": len(tasks),
    }


@router.get("/view-queue")
def view_queue():
    tasks = lists.lrange("tasks")
    return {
        "команда": "LRANGE tasks 0 -1",
        "очередь": tasks,
        "размер": len(tasks),
    }

@router.get("/process-task")
def process_task():
    if lists.llen("tasks") == 0:
        lists.rpush("tasks", "task1", "task2", "task3")

    task = lists.lpop("tasks")
    remaining = lists.lrange("tasks")

    return {
        "команда": "LPOP tasks",
        "обработанная_задача": task,
        "осталось_в_очереди": remaining,
    }

@router.get("/job-queue")
def job_queue():
    strings.delete("jobs")
    lists.rpush("jobs", "send_email", "resize_image")
    all_jobs = lists.lrange("jobs")
    processed = lists.lpop("jobs")
    remaining = lists.lrange("jobs")

    return {
        "добавлены": all_jobs,
        "обработана": processed,
        "осталось": remaining,
        "пояснение": f"Worker взял задачу '{processed}' в работу",
    }

