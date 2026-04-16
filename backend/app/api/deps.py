from fastapi import APIRouter, Depends, HTTPException, status
import jwt
from jose import JWTError
from dotenv import load_dotenv
import os

from app.core.database import SessionLocal
from app.core.security import oauth2_scheme
from app.models.user import User

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token = Depends(oauth2_scheme), db = Depends(get_db)):
    # check if token works
    # decode token
    # extract user_id from token
    # query for the user
    # if not found --> error, otherwise return user

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )
    decoded_token = jwt.decode(token,SECRET_KEY, algorithms=[ALGORITHM])

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},)

    user_id = decoded_token.get("user_id")    

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    
    user = db.query(User).filter(User.user_id == user_id).first()
    if user is None:
        raise credentials_exception
    
    return user


