from typing import Optional

from pydantic import BaseModel


class Tasks(BaseModel):
    name: str
    description: str
    age: Optional[int]


class STask(BaseModel):
    id: int


class STaskID(BaseModel):
    ok: bool = True
    task_id: int
