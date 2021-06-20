from fastapi import APIRouter

from endpoints import users,payments

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(payments.router, prefix="/payments", tags=["payments"])