from fastapi import FastAPI

from decouple import config
import psycopg2
import pandas as pd
import gspread
from gspread_dataframe import set_with_dataframe

from infrastructure.data import model
from infrastructure.data.database import engine

from controllers import knowledge_controller


from fastapi.middleware.cors import CORSMiddleware

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(knowledge_controller.router)
