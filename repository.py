from sqlalchemy import select
from database import new_session, EntryORM
from schemas import Entry, EntryAdd


# work with db, CRUD


class EntryRepository:
    @classmethod
    async def add_one(cls, data: EntryAdd) -> int:
        """"""
        async with new_session() as session:
            entry_dict = data.model_dump()  # -> dict
            entry = EntryORM(**entry_dict)  # -> unpackage in TaskORM
            session.add(entry)  # add session
            await session.flush()  # send to DB, not finish transaction -> get ID, return ID new obj
            await session.commit()  # commit DB
            return entry.id

    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(EntryORM)
            result = await session.execute(query)
            entry_models = result.scalars().all()  # returned objs
            # entry_schemas = [Entry.model_validate(entry_model) for entry_model in entry_models]
            return entry_models

    @classmethod
    async def find_by_id(cls, entry_id):
        async with new_session() as session:
            query = select(EntryORM).filter(EntryORM.id == entry_id)
            result = await session.execute(query)
            entry = result.scalar_one_or_none()
            return entry

    @classmethod
    async def put_entry_id(cls, entry_id, data):
        async with new_session() as session:
            query = select(EntryORM).filter(EntryORM.id == entry_id)
            result = await session.execute(query)
            entry = result.scalar_one_or_none()   # object in DB
            # print(result)
            if entry:
                for key, value in data.items():
                    setattr(entry, key, value)
                # if 'name' and 'description' and 'age' in data:
                #     entry.data = data['name']
                #     entry.description = data['description']
                #     entry.age = data['age']
                await session.commit()
            return entry

    @classmethod
    async def delete_entry_id(cls, entry_id):
        async with new_session() as session:
            query = select(EntryORM).filter(EntryORM.id == entry_id)
            result = await session.execute(query)
            entry = result.scalar_one_or_none()
            entry_id = entry.id
            session.delete(entry)
            session.commit()
            return {'entry_id': entry_id}

