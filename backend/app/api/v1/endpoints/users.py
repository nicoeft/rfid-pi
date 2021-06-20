from typing import Any, List
from fastapi import APIRouter, Depends
import sys
from os import path

sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from api import deps


router = APIRouter()


@router.get("/")
def read_users(
        db = Depends(deps.get_db)
) -> Any:
    """
    Retrieve users.
    """
    users = db.query(User).all()
    return users


@router.get("/{user_id}")
def read_user_by_id(
        user_id: int,
        db = Depends(deps.get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    user = db.query(User).get(user_id)
    return user
