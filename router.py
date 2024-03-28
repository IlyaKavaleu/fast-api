from fastapi import APIRouter, Depends, Request, HTTPException
from typing import Any, Annotated

from starlette import status

from repository import EntryRepository
from schemas import EntryAdd, Entry, EntryID, EntryEdit

entries_router = APIRouter(
    prefix='/tasks',
    tags=['Tasks']
)


@entries_router.post('')
async def add_entry(entry: Annotated[EntryAdd, Depends()]) -> EntryID:
    entry_id = await EntryRepository.add_one(entry)
    return {'entry_id': entry_id}


@entries_router.get('')
async def get_tasks():
    tasks = await EntryRepository.find_all()
    return {'tasks': tasks}


@entries_router.get('/{entry_id}', response_model=Entry)
async def entry_detail(entry_id: int):
    entry = await EntryRepository.find_by_id(entry_id)
    return entry


@entries_router.put('/{entry_id}', response_model=EntryEdit)
async def put_entry_by_id(entry_id: int, data: Annotated[EntryEdit, Depends()]):
    entry = await EntryRepository.put_entry_id(entry_id, data.dict())
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return entry


@entries_router.delete('/{entry_id}')
async def delete_entry_by_id(entry_id: int):
    entry = await EntryRepository.delete_entry_id(entry_id)
    return entry
