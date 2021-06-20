from fastapi import APIRouter
import sys
from os import path
#Import from siblings
sys.path.append(path.dirname(path.abspath(__file__)))
from endpoints import users,payments

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(payments.router, prefix="/payments", tags=["payments"])
