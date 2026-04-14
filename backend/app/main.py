from fastapi import Depends, FastAPI

from functools import lru_cache
from typing import Annotated

from core import config

app = FastAPI()

@lru_cache
def get_settings():
    return config.Settings()

# endpoints 
@app.get("/")
async def root():
    return {"message": "hey World"}
