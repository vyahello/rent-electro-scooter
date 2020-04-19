from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.orm import relation
from scooter.models import BaseModel
from scooter.models.rentals import Rental


class User(BaseModel):
    """The class represents users table.

    Class variables are fields of a table.
    """

    __tablename__: str = "users"
    id: Column = Column(Integer, primary_key=True, autoincrement=True)
    name: Column = Column(String, nullable=True)
    gender: Column = Column(String, nullable=True)
    email: Column = Column(String, index=True, nullable=True, unique=True)
    hashed_password: Column = Column(String, nullable=True, index=True)
    created_date: Column = Column(DateTime, default=datetime.now, index=True)
    last_login: Column = Column(DateTime, default=datetime.now, index=True)
    rentals = relation("Rental", order_by=[Rental.start_time.desc()], back_populates="user")
