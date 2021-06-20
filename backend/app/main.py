from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.v1.api import api_router
from core import config

app = FastAPI()

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=config.API_V1_STR)
