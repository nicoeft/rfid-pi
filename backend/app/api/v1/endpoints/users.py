from typing import Any

from fastapi import APIRouter, Depends, Body

from app.api import deps
from app.models import Transaction
from app.models.user import User

router = APIRouter()


@router.get("/")
def read_users(
        db=Depends(deps.get_db)
) -> Any:
    """
    Retrieve users.
    """
    users = db.query(User).all()
    return users

@router.post("/")
def create_user(
        user: User,
        db = Depends(deps.get_db)
) -> Any:
    """
    Create user.
    """
    db.add(user)
    db.commit()
    return user


@router.get("/{user_id}")
def read_user_by_id(
        user_id: int,
        db=Depends(deps.get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    user = db.query(User).get(user_id)
    return user


@router.get("/{user_id}/transactions")
def read_user_transactions(
        user_id: int,
        db=Depends(deps.get_db),
) -> Any:
    """
    Get all user's transactions
    """
    transactions = db.query(Transaction).filter_by(user_id=user_id).all()
    return transactions


@router.post("/{user_id}/rfid_uuid")
def set_rfid_uuid(
        user_id: int,
        rfid_uuid: str = Body(...),
        db=Depends(deps.get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    user = db.query(User).get(user_id)
    user.rfid_uuid = rfid_uuid
    db.commit()
    return user


@router.post("/{user_id}/deposit/{amount}")
def deposit(
        user_id: int,
        amount: int,
        db=Depends(deps.get_db),
) -> Any:
    """
    Deposit amount to a specific user.
    """
    user = db.query(User).get(user_id)
    user.balance += amount
    db.commit()
    return user


@router.post("/{user_id}/withdraw/{amount}")
def withdraw(
        user_id: int,
        amount: int ,
        db=Depends(deps.get_db),
) -> Any:
    """
    Withdraw amount from  a specific user.
    """
    user = db.query(User).get(user_id)
    user.balance -= amount
    db.commit()
    return user
