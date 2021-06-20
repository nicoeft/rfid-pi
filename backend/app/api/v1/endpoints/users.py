from typing import Any, List
from fastapi import APIRouter, Depends, Body, HTTPException

from app.api import deps
from app.models import Transaction
from app.models.user import User



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


@router.get("/{user_id}/transactions")
def read_user_transactions(
        user_id: int,
        db = Depends(deps.get_db),
) -> Any:
    """
    Get all user's transactions
    """
    users = db.query(Transaction).find_by(user_id=user_id)
    return

@router.post("/{user_id}/rfid_uuid")
def set_rfid_uuid(
        user_id: int ,
        rfid_uuid: str = Body(...),
        db = Depends(deps.get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    user = db.query(User).get(user_id)
    user.rfid_uuid = rfid_uuid
    db.commit()
    return user


@router.post("/{user_id}/deposit")
def deposit(
        user_id: int ,
        amount: float = Body(...),
        db = Depends(deps.get_db),
) -> Any:
    """
    Deposit amount to a specific user.
    """
    user = db.query(User).get(user_id)
    if amount > 0:
        user.balance += amount
        db.commit()
        return user
    else:
        raise HTTPException(
            status_code=400,
            detail="Amount to deposit must be positive",
        )

@router.post("/{user_id}/withdraw")
def withdraw(
        user_id: int ,
        amount: float = Body(...),
        db = Depends(deps.get_db),
) -> Any:
    """
    Withdraw amount from  a specific user.
    """
    user = db.query(User).get(user_id)
    if amount > 0:
        user.balance -= amount
        db.commit()
        return user
    else:
        raise HTTPException(
            status_code=400,
            detail="Amount to withdraw must be positive",
        )