import json
from typing import Any, List
from fastapi import APIRouter, Depends

from app.api import deps
from app.models import Provider, Transaction
from app.models.user import User



router = APIRouter()


@router.get("/")
def read_providers(
        db = Depends(deps.get_db)
) -> Any:
    """
    Retrieve providers.
    """
    providers = db.query(Provider).all()
    return providers


@router.get("/{provider_id}")
def read_provider_by_id(
        provider_id: int,
        db = Depends(deps.get_db),
) -> Any:
    """
    Get a specific provider by id.
    """
    provider = db.query(Provider).get(provider_id)
    return provider


@router.get("/{provider_id}/transactions")
def read_provider_transactions(
        provider_id: int,
        db = Depends(deps.get_db),
) -> Any:
    """
    Get all provider's transactions
    """
    transactions = db.query(Transaction).filter_by(provider_id=provider_id)
    print(transactions)
    print(json.dumps(transactions))
    return json.dumps(transactions)
