from datetime import datetime

from leopard_id.database import Database
from leopard_id.database.models import Review

class ReviewRepository:
    """Provide database operations for Review objects."""


    def __init__(self, database: Database) -> None:
        self.database = database

    def add(self, review: Review) -> int:
        """Add a review to the database and return its database ID."""
        cursor = self.database.execute(
            """
            INSERT INTO reviews (
                image_id,
                prediction_id,
                decision,
                reviewer,
                corrected_prediction,
                notes
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                review.image_id,
                review.prediction_id,
                review.decision,
                review.reviewer,
                review.corrected_prediction,
                review.notes
            ),
        )

        self.database.commit()

        return cursor.lastrowid

    def get(self, review_id: int) -> Review | None:
        """Return the review with the given ID, or None if it doesn't exist."""
        cursor = self.database.execute(
            """
            SELECT
                id,
                image_id,
                prediction_id,
                decision,
                reviewer,
                corrected_prediction,
                notes,
                db_created_at
            FROM reviews
            WHERE id = ?
            """,
            (review_id,),
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return self._row_to_seal(row)


    def delete(self, review_id: int) -> None:
        """Delete a review from the database."""
        self.database.execute(
            """
            DELETE FROM reviews
            WHERE id = ?
            """,
            (review_id,),
        )

        self.database.commit()

    @staticmethod
    def _row_to_review(row) -> Review:
        """Convert a database row into a Seal object."""
        return Review(
            review_id=row["id"],
            image_id=row["image_id"],
            prediction_id=row["prediction_id"],
            decision=row["decision"],
            reviewer=row["reviewer"],
            corrected_prediction=row["corrected_prediction"],
            notes=row["notes"],
            db_created_at=row["db_created_at"]
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