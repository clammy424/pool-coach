from fastapi import FastAPI
from functools import lru_cache

from app.core import config
from app.api.v1.auth import router as auth_router
from app.api.v1.users import router as users_router
from app.core.database import init_db

def lifespan(app: FastAPI):
    # Startup: Load database pool, ML models, etc.
    print("Application is starting up")
    init_db()
    yield
    # Shutdown: Close connections, clean up resources
    print("Application is shutting down")

app = FastAPI(lifespan=lifespan)
    
@lru_cache
def get_settings():
    return config.Settings()

# endpoints 
@app.get("/")
async def root():
    return {"message": "hey World"}

app.include_router(auth_router, prefix="/api/v1")
app.include_router(users_router, prefix="/api/v1")
