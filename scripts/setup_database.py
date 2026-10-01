import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

load_dotenv()

DATABASE_NAME = "leopard_id"


def database_exists(admin_url: str) -> bool:
    """Return whether the project database already exists."""

    engine = create_engine(admin_url)

    with engine.connect() as connection:
        result = connection.execute(
            text(
                """
                SELECT 1
                FROM pg_database
                WHERE datname = :database_name
                """
            ),
            {"database_name": DATABASE_NAME},
        )

        return result.scalar() is not None


def create_database(admin_url: str) -> None:
    """Create the project database if it does not already exist."""

    if database_exists(admin_url):
        print(f"Database '{DATABASE_NAME}' already exists.")
        return

    engine = create_engine(
        admin_url,
        isolation_level="AUTOCOMMIT",
    )

    with engine.connect() as connection:
        connection.execute(
            text(f'CREATE DATABASE "{DATABASE_NAME}"')
        )

    print(f"Created database '{DATABASE_NAME}'.")


if __name__ == "__main__":
    admin_url = os.environ["POSTGRES_ADMIN_URL"]

    create_database(admin_url)