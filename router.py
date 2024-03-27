from fastapi import APIRouter, Depends
from typing import Any, Annotated
from repository import TaskRepository
from schemas import STask, Tasks, STask, STaskID

router = APIRouter(
    prefix='/tasks',
    tags=['Tasks']
)


@router.post('')
async def add_task(task: Annotated[Tasks, Depends()]) -> STaskID:
    task_id = await TaskRepository.add_one(task)
    return {'task_id': task_id}


@router.get('')
async def get_tasks():
    tasks = await TaskRepository.find_all()
    return {'tasks': tasks}
