from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

class Record(Base):
    __tablename__ = "records"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    value: Mapped[str] = mapped_column(String(50))