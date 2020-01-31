from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from scooter.database.storage import full_path

__engine = None
__factory = None


class InitError(Exception):
    """Represents session exception."""

    def __init__(self) -> None:
        super().__init__("You have not created global init")


def global_init(database_name: str) -> None:
    """Initializes sessions."""
    global __engine, __factory

    if __factory:
        return

    connection: str = f"sqlite:///{full_path(database_name)}"
    __engine = create_engine(connection, echo=False)
    __factory = sessionmaker(bind=__engine)


def create_tables() -> None:
    """Create database tables."""
    if not __engine:
        raise InitError

    # noinspection PyUnresolvedReferences
    import scooter.models.__models  # noqa: F401, pylint: disable=import-outside-toplevel
    from scooter.models.base import BaseModel  # pylint: disable=import-outside-toplevel

    BaseModel.metadata.create_all(__engine)


def create_session() -> Session:
    """Create database session."""
    if not __factory:
        raise InitError

    session: Session = __factory()
    session.expire_on_commit = False
    return session
