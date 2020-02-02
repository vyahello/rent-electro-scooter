from datetime import datetime, timedelta
from random import choice, randint
from typing import List
from sqlalchemy.orm import Session
from scooter.models.locations import Location
from scooter.models.rentals import Rental
from scooter.models.scooters import Scooter
from scooter.models.sessions import create_session
from scooter.models.users import User
from scooter.services.service import default_user, book_scooter, part_scooter


def __import_locations() -> None:
    """Imports location services."""
    session: Session = create_session()
    if session.query(Scooter).count() > 0:
        return
    location = Location()
    location.street = "544 Main St."
    location.state = "OR"
    location.city = "Lviv"
    location.max_storage = randint(10, 20)
    session.add(location)

    location = Location()
    location.street = "700 Shevchenko Blvd"
    location.state = "OR"
    location.city = "Kyiv"
    location.max_storage = randint(10, 20)
    session.add(location)

    location = Location()
    location.street = "700 Broadway"
    location.state = "OR"
    location.city = "Lviv"
    location.max_storage = randint(10, 20)
    session.add(location)
    session.commit()


def __import_scooters() -> None:
    """Imports scooters services."""
    session: Session = create_session()
    if session.query(Scooter).count() > 0:
        return
    models: List[str] = [
        "Hover-1 1st edition",
        "Hover-1 Sport 1st edition",
        "Hover-1 Touring 1st edition",
        "Hover-1 2nd edition",
        "Hover-1 Sport 2nd edition",
        "Hover-1 Touring 2nd edition",
        "Hover-1 3rd edition",
        "Hover-1 Sport 3rd edition",
        "Hover-1 Touring 3rd edition",
    ]
    vin_values: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    locations: List[Location] = list(session.query(Location).all())
    count: int = 21
    for _ in range(0, count):
        scooter = Scooter()
        scooter.model = choice(models)
        scooter.battery_level = 100
        scooter.vin = "".join((choice(vin_values) for _ in range(0, 18)))
        scooter.location = choice(locations)
        session.add(scooter)
    session.commit()


def __import_users() -> None:
    """Imports users services."""
    session: Session = create_session()
    if session.query(User).count() > 0:
        return
    default_user()
    user = User()
    user.email = "user@gmail.com"
    user.name = "user 2"
    session.add(user)
    session.commit()


def __import_rentals() -> None:
    """Imports rentals services."""
    session: Session = create_session()
    if session.query(Rental).count() > 0:
        return
    scooters: List[Scooter] = list(session.query(Scooter))
    locations: List[Scooter] = list(session.query(Location))
    user: User = default_user()
    user2: User = session.query(User).filter(User.email == "user@gmail.com").one()

    for _ in range(1, 3):
        selected: Scooter = choice(scooters)
        book_scooter(scooter=selected, user=user, start_data=datetime.now() - timedelta(days=randint(1, 100)))
        scooters.remove(selected)
        part_scooter(selected.id, choice(locations).id)

    for _ in range(1, 10):
        selected = choice(scooters)
        book_scooter(scooter=selected, user=user2, start_data=datetime.now() - timedelta(days=randint(1, 100)))
        scooters.remove(selected)


def import_database() -> None:
    """Imports database services."""
    __import_locations()
    __import_scooters()
    __import_users()
    __import_rentals()
