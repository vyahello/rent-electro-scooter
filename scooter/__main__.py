import datetime
import sys
from typing import List
from scooter.import_ import import_database
from scooter.infrastructure.numbers import make_int
from scooter.infrastructure.switch import Switch
from scooter.models.scooters import Scooter
from scooter.models.sessions import create_tables, global_init
from scooter.models.users import User
from scooter.services.service import default_user, parked_scooters, book_scooter, rented_scooters

user: User = None


def launch_scooter_rental() -> None:
    """Launch scooter rental program."""
    setup_database()
    print()
    print(f"{f'':*^100}")
    print(f"{f' Electro scooter rental application ':*^100}")
    print(f"{f'':*^100}")
    print()
    options: str = "Please choose a command, [r]ent, [a]vailable, [l]ocate, [h]istory, [q]uit: "
    command: str = "NOT SET"

    while command:
        command = input(options).lower().strip()
        with Switch(command) as switch:
            switch.case("r", rent_scooter)
            switch.case("a", available_scooters)
            switch.case("l", locate_scooters)
            switch.case("h", history)
            switch.case(["q", "e"], exit_application)
            switch.default(lambda: print(f"Don't know what to do with {command} command."))


def setup_database() -> None:
    """Proceed with global database setup."""
    global user
    global_init("scooter.sqlite")
    create_tables()
    import_database()
    user = default_user()


def available_scooters(suppress_header: bool = False) -> List[Scooter]:
    """Returns list of available scooters."""
    if not suppress_header:
        print(f"{f' Available scooters ':*^100}")

    list_of_parked_scooters: List[Scooter] = parked_scooters()
    for index, scooter in enumerate(list_of_parked_scooters, start=1):  # type: int, Scooter
        print(
            f"#{index}. Loc: {scooter.location.street} {scooter.location.city}, "
            f"{scooter.id} {scooter.model} VIN: {scooter.vin} with battery level {scooter.battery_level}%"
        )
    print()
    return list_of_parked_scooters


def rent_scooter() -> None:
    """Rents a scooter option."""
    print(f"{f' Rent a scooter ':*^100}")
    scooters: List[Scooter] = available_scooters(True)
    chose: int = make_int(input("Which one do you want? ")) - 1

    if not (chose >= 0 or chose < len(scooters)):
        print("Error: Pick another number.")
        return

    scooter: Scooter = scooters[chose]
    book_scooter(scooter, user, datetime.datetime.now())


def locate_scooters() -> None:
    """Locates our booked scooters."""
    print(f"{f' Current location of our scooters  ':*^100}")

    list_of_rented_scooters: List[Scooter] = rented_scooters()
    list_of_parked_scooters: List[Scooter] = parked_scooters()

    print(f"Out with clients [{len(list_of_rented_scooters)} scooters]:")
    for rented in list_of_rented_scooters:  # type: Scooter
        print(f" {rented.id} {rented.model} VIN: {rented.vin} with battery level {rented.battery_level}%")

    print()

    print(f"Parked [{len(list_of_parked_scooters)} scooters]:")
    for parked in list_of_parked_scooters:  # type: Scooter
        print(
            f"Location: {parked.location.street} {parked.location.city}, "
            f"{parked.id} {parked.model} VIN: {parked.vin} with battery level {parked.battery_level}%"
        )


def history() -> None:
    """Checks user history list."""
    print(f"{f' Your rental history  ':*^100}")
    local: User = default_user()
    for rental in local.rentals:
        print(f" * {rental.start_time.date().isoformat()} {rental.scooter.model}")


def exit_application():
    """Exits an application."""
    print("")
    print("Thanks for usage, good bye!")
    sys.exit(0)


if __name__ == "__main__":
    launch_scooter_rental()
