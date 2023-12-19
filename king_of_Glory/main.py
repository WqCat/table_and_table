"""
@Time: 2023/12/13 20:00
@Author: WQ
@File: main.py
@Des:
"""
import uvicorn
from fastapi import FastAPI

from king_of_Glory.api.endpoints.api import api_router

app = FastAPI()

app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
