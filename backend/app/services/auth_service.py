from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password, verify_password

def create_user(db: Session, user_create: UserCreate):
    # Check if email already exists
    existing_user = db.query(User).filter(User.email == user_create.email).first()
    if existing_user:
        raise ValueError("Email already registered")
    # Hash password
    hashed_pwd = hash_password(user_create.password)

    # Create DB user
    new_user = User(
        email = user_create.email,
        hashed_password = hashed_pwd
    )

    # Save to database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Return the user
    return new_user


def authenticate_user(db: Session, email: str, password: str):
    # get user/username
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

