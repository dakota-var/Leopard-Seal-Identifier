from datetime import datetime

from leopard_id.database import Database
from leopard_id.database.models import Seal


class SealRepository:
    """Provide database operations for Seal objects."""

    def __init__(self, database: Database) -> None:
        self.database = database

    def add(self, seal: Seal) -> int:
        """Add a seal to the database and return its database ID."""
        cursor = self.database.execute(
            """
            INSERT INTO seals (
                sex,
                first_seen,
                last_seen,
                notes,
                images
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                seal.sex,
                seal.first_seen,
                seal.last_seen,
                seal.notes,
                seal.images
            ),
        )

        self.database.commit()

        return cursor.lastrowid

    def get(self, seal_id: int) -> Seal | None:
        """Return the seal with the given ID, or None if it doesn't exist."""
        cursor = self.database.execute(
            """
            SELECT
                id,
                sex,
                first_seen,
                last_seen,
                notes
            FROM seals
            WHERE id = ?
            """,
            (seal_id,),
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return self._row_to_seal(row)

    def update(self, seal: Seal) -> None:
        """Update an existing seal in the database."""
        self.database.execute(
            """
            UPDATE seals
            SET
                sex = ?,
                first_seen = ?,
                last_seen = ?,
                notes = ?
            WHERE id = ?
            """,
            (
                seal.sex,
                seal.first_seen,
                seal.last_seen,
                seal.notes,
                seal.id,
            ),
        )

        self.database.commit()

    def delete(self, seal_id: int) -> None:
        """Delete a seal from the database."""
        self.database.execute(
            """
            DELETE FROM seals
            WHERE id = ?
            """,
            (seal_id,),
        )

        self.database.commit()

    @staticmethod
    def _row_to_seal(row) -> Seal:
        """Convert a database row into a Seal object."""
        return Seal(
            seal_id=row["id"],
            sex=row["sex"],
            first_seen=row["first_seen"],
            last_seen=row["last_seen"],
            notes=row["notes"]
        )

    @staticmethod
    def _datetime_to_string(value: datetime | None) -> str | None:
        """Convert a datetime to an ISO-8601 string for SQLite."""
        if value is None:
            return None

        return value.isoformat()

    @staticmethod
    def _string_to_datetime(value: str | None) -> datetime | None:
        """Convert an ISO-8601 string from SQLite into a datetime."""
        if value is None:
            return None

        return datetime.fromisoformat(value)