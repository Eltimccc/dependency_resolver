from fastapi import APIRouter
from app.api.validators import (
    validate_build_exists,
    validate_build_request,
    validate_data,
)
from app.services.tasks_sort import get_sorted_tasks
from app.core.config import tasks, builds

router = APIRouter()


@router.post(
    "/get_tasks",
    tags=("Таски для введенного билда",),
    summary="get tasks for build",
    response_description="Таски ввиде json",
)
async def get_tasks(build: str):
    """
    Список тасок для билда:

    - **build**: название билда из builds/builds.yaml
    """
    validate_build_request(build)
    validate_data()
    validate_build_exists(build, builds["builds"])
    sorted_tasks = get_sorted_tasks(build, tasks["tasks"], builds)

    return {"tasks": sorted_tasks}
