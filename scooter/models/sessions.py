from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker
from scooter.database.storage import full_path

__engine: Engine = None
__factory: sessionmaker = None


class InitError(Exception):
    """Represents session exception."""

    def __init__(self, name: str) -> None:
        super().__init__(f"You have not created global init for {name} target")


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
        raise InitError(name="tables")

    # noinspection PyUnresolvedReferences
    import scooter.models.__models  # noqa: F401, pylint: disable=import-outside-toplevel
    from scooter.models import BaseModel  # pylint: disable=import-outside-toplevel

    BaseModel.metadata.create_all(__engine)


def create_session() -> Session:
    """Create database session."""
    if not __factory:
        raise InitError(name="session")

    session: Session = __factory()
    session.expire_on_commit = False
    return session
