from typing import Optional

from pydantic import BaseModel


class EntryAdd(BaseModel):
    name: str
    description: str | None
    age: Optional[int]


class EntryEdit(BaseModel):
    name: str
    description: str | None
    age: Optional[int]


class Entry(EntryAdd):
    id: int


class EntryID(BaseModel):
    ok: bool = True
    entry_id: int
