from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.orm import relation
from scooter.models import BaseModel


class Rental(BaseModel):
    """The class represents rentals table.

    Class variables are fields of a table.
    """

    __tablename__: str = "rentals"
    id: Column = Column(Integer, primary_key=True, autoincrement=True)
    created_date: Column = Column(DateTime, default=datetime.now, index=True)
    start_time: Column = Column(DateTime, default=datetime.now, index=True)
    end_time: Column = Column(DateTime, index=True)
    user_id: Column = Column(Integer, ForeignKey("users.id"), nullable=False)
    scooter_id: Column = Column(String, ForeignKey("scooters.id"), nullable=False)
    user = relation("User", back_populates="rentals")
    scooter = relation("Scooter")
