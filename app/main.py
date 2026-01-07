from fastapi import FastAPI
from app.api import records, auth
from app.db.base import Base
from app.db.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Demo Service")

app.include_router(auth.router)
app.include_router(records.router)