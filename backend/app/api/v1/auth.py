from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserResponse
from app.services.auth_service import create_user, authenticate_user
from app.api.deps import get_db
from app.core.security import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserResponse)

def register(user: UserCreate, db: Session = Depends(get_db)):
    try:
        new_user = create_user(db, user)
        return new_user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.post("/login")

def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = authenticate_user(db, user.email, user.password)

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    token = create_access_token(
        data={"user_id": db_user.user_id}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }