from pydantic import BaseModel

class RecordCreate(BaseModel):
    name: str
    status: str

class RecordRead(RecordCreate):
    id: int

    class Config:
        from_attributes = True