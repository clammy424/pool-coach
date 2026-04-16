from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
import os
import jwt
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, status

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = int(os.getenv("TOKEN_EXPIRE_MINUTES"))


# PASSWORD HASHING
pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto"
)
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")
