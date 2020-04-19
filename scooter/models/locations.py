from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.orm import relation
from scooter.models import BaseModel


class Location(BaseModel):
    """The class represents locations table.

    Class variables are fields of a table.
    """

    __tablename__: str = "location"
    id: Column = Column(Integer, primary_key=True, autoincrement=True)
    created_data: Column = Column(DateTime, default=datetime.now, index=True)
    street: Column = Column(String)
    city: Column = Column(String, index=True)
    state: Column = Column(String, index=True)
    postal: Column = Column(String, index=True)
    max_storage = Column(Integer, index=True)
    scooters = relation("Scooter", back_populates="location")
