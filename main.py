from typing import Union
from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/v1/get-endday/{ticket}")
async def get_endday(ticket: str):
    resp = (requests.get(
        f'https://yobit.net/api/3/ticker/{ticket}_usdt')).json()
    if 'error' in resp.keys():
        return {"error_code": resp['error']}
    else:
        return {"pair": f'{ticket}_usdt', "price": resp[f'{ticket}_usdt']['avg']}


@app.get("/v1/get-symbol/{ticket}")
async def get_symbol(ticket: str):
    resp = (requests.get(
        f'https://yobit.net/api/3/ticker/{ticket}_usdt')).json()
    if 'error' in resp.keys():
        return {"error_code": resp['error']}
    else:
        return {"pair": f'{ticket}_usdt', "price": resp[f'{ticket}_usdt']['last']}
