# pylint: disable=singleton-comparison
from datetime import datetime, timedelta
from random import randint
from typing import List
from sqlalchemy.orm import Session
from scooter.models.rentals import Rental
from scooter.models.scooters import Scooter
from scooter.models.users import User
from scooter.models.sessions import create_session


def default_user() -> User:
    """Returns default user."""
    session: Session = create_session()
    user = session.query(User).filter(User.email == "test@gmail.com").first()
    if user:
        return user

    user = User()
    user.email = "test@gmail.com"
    user.name = "Test user 1"
    session.add(user)
    session.commit()
    return user


def book_scooter(scooter: Scooter, user: User, start_data: datetime) -> Rental:
    """Books a scooter."""
    session: Session = create_session()
    scooter = session.query(Scooter).filter(Scooter.id == scooter.id).one()
    scooter.location_id = None
    scooter.battery_level = randint(50, 100)
    rental = Rental()
    rental.scooter_id = scooter.id
    rental.user_id = user.id
    rental.start_time = start_data
    rental.end_time = rental.start_time + timedelta(days=1)
    session.add(rental)
    session.commit()
    return rental


def part_scooter(scooter_id: int, location_id: int) -> Scooter:
    """Parks a scooter."""
    session: Session = create_session()
    scooter = session.query(Scooter).filter(Scooter.id == scooter_id).one()
    scooter.location_id = location_id
    scooter.battery_level = 100
    session.commit()
    return scooter


def rented_scooters() -> List[Scooter]:
    """Returns list of rented scooters."""
    return list(create_session().query(Scooter).filter(Scooter.location_id == None).all())  # noqa: E711


def parked_scooters() -> List[Scooter]:
    """Returns list of parked scooters."""
    return list(create_session().query(Scooter).filter(Scooter.location_id != None).all())  # noqa: E711
