from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.orm import relation
from scooter.models import BaseModel


class Scooter(BaseModel):
    """The class represents scooters table.

    Class variables are fields of a table.
    """

    __tablename__: str = "scooters"
    id: Column = Column(Integer, primary_key=True, autoincrement=True)
    created_date: Column = Column(DateTime, default=datetime.now)
    vin: Column = Column(String, index=True, unique=True)
    model: Column = Column(String, index=True)
    battery_level: Column = Column(Integer, index=True)
    location_id: Column = Column(Integer, ForeignKey("location.id"), nullable=True)
    location = relation("Location")
