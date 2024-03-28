from typing import Optional
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine(   # async engine
    'sqlite+aiosqlite:///tasks.db'
)


new_session = async_sessionmaker(engine, expire_on_commit=False)   # fabric transaction for work with db, create session
                                                                   # session let work with db like with models


class Model(DeclarativeBase):
    ...


class EntryORM(Model):
    __tablename__ = "entries"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]
    description: Mapped[Optional[str]]
    age: Mapped[Optional[int]]


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)

