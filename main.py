from asyncio import Task
from fastapi import FastAPI, Request, Depends, security, HTTPException
from fastapi.security import HTTPBasicCredentials
from pydantic import BaseModel, ValidationError, validator, EmailStr
from starlette import status
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from schemas import *
from router import entries_router


def fake_answer_to_everything_mk_model(x: float):
    return x * 42


ml_models = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    # await delete_tables()
    print('Base clear')
    await create_tables()
    print('Base ready')
    yield
    print('Off DB')


app = FastAPI(lifespan=lifespan)
app.include_router(entries_router)

# app = FastAPI(
#     title='Py=44 TEST API',
#     description='Very big text',
#     openapi_url='/api/openapi.json',
#     docs_url='/api/docs',
#     version='1.0.0'
# )
#
#
# class AccDataK(BaseModel):
#     items: list
#
#     @validator('items')
#     def items_validator(cls, value):
#         try:
#             return list(value)
#         except Exception:
#             raise ValueError('Invalid data')
#
#
# class AccDataV(BaseModel):
#     items: tuple
#
#
# class AccDataResp(BaseModel):
#     keys: AccDataK
#     values: AccDataV
#
#
# class NewUser(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#
#
# @app.get('/')
# async def root():
#     return {'message': 'Hello World'}
#
#
# @app.get('/hello/{name}')
# async def say_hello(name: str, req: Request):
#     return {'message': f'Hello {name}', 'data': req.headers}
#
#
# @app.get('/list')
# async def get_dict(data: dict, req: Request):
#     return {'data': req.headers, 'Dict Data': data.items()}
#
#
# @app.post('/account', response_model=AccDataResp)
# async def account(data: dict) -> AccDataResp:
#     return AccDataResp(keys=AccDataK(items=list(data.keys())), values=AccDataV(items=tuple(data.values())))
