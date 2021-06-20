from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api import deps
from app.models.user import User

router = APIRouter()


@router.get("/", response_model=List[User])
def read_users(
        db: Session = Depends(deps.get_db)
) -> Any:
    """
    Retrieve users.
    """
    users = db.query(User).all()
    return users


@router.get("/{user_id}", response_model=User)
def read_user_by_id(
        user_id: int,
        db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    user = db.query(User).get(user_id)
    return user
