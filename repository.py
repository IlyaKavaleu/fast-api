from sqlalchemy import select
from database import new_session, TaskORM
from schemas import STask, Tasks


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STask) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()
            task = TaskORM(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(TaskORM)
            result = await session.execute(query)
            task_models = result.scalars().all()
            return task_models
