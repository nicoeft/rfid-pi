from typing import Any, List

from fastapi import APIRouter, Depends, Body

from api import deps


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
