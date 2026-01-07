from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.security import get_current_user
from app.db.session import SessionLocal
from app.db.models import Record
from app.schemas.records import RecordCreate, RecordRead

router = APIRouter(prefix="/records", tags=["records"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=RecordRead)
def create_record(
    data: RecordCreate, 
    db: Session = Depends(get_db), 
    user: dict = Depends(get_current_user)
    ):
    record = Record(**data.model_dump())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

@router.get("/", response_model=List[RecordRead])
def list_records(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
    ):
    return db.query(Record).offset(skip).limit(limit).all()