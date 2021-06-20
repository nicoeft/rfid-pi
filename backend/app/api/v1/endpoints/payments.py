from typing import Any, List

from fastapi import APIRouter, Depends, Body

from app.api import deps
from app.models.user import User

router = APIRouter()


@router.post("/")
def read_user_by_id(
        user_id: int = Body(...),
        amount: float = Body(...),
        db = Depends(deps.get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    user = db.query(User).get(user_id)
    user.balance += amount
    db.commit()
    return user
