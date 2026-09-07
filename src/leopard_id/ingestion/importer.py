"""Import image metadata into the database."""

import csv
from datetime import datetime
from pathlib import Path

from ..database import Database

class INaturalistImporter:
    """Import image metadata from iNaturalist."""

    def __init__(self, database: Database) -> None:
        self.database = database

    def import_csv(self, path: str | Path) -> int:
        """Import image metadata from an iNaturalist CSV export.

        Args:
            path: Path to the CSV file.

        Returns:
            The number of images successfully imported.
        """
        path = Path(path)
        imported = 0

        with path.open("r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                self._import_inat_row(row)
                imported += 1

        self.database.commit()

        return imported

    def _import_inat_row(self, row: dict[str, str]) -> None:
        """Import a single CSV row into the images table."""
        self.database.execute(
            """
            INSERT INTO images (
                file_path,
                source,
                source_id,
                captured_at,
                latitude,
                longitude,
                licence,
                attribution
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                row["file_path"],
                row.get("source"),
                row.get("source_id"),
                self._parse_datetime(row.get("captured_at")),
                self._parse_float(row.get("latitude")),
                self._parse_float(row.get("longitude")),
                row.get("licence"),
                row.get("attribution"),
            ),
        )

class ImageImporter:
    """Import image metadata from external data sources."""

    def __init__(self, database: Database) -> None:
        self.database = database

    def import_csv(self, path: str | Path) -> int:
        """Import image metadata from a CSV file.

        Args:
            path: Path to the CSV file.

        Returns:
            The number of images successfully imported.
        """
        path = Path(path)
        imported = 0

        with path.open("r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                self._import_row(row)
                imported += 1

        self.database.commit()

        return imported

    def _import_row(self, row: dict[str, str]) -> None:
        """Import a single CSV row into the images table."""
        self.database.execute(
            """
            INSERT INTO images (
                file_path,
                source,
                source_id,
                captured_at,
                latitude,
                longitude,
                licence,
                attribution
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                row["file_path"],
                row.get("source"),
                row.get("source_id"),
                self._parse_datetime(row.get("captured_at")),
                self._parse_float(row.get("latitude")),
                self._parse_float(row.get("longitude")),
                row.get("licence"),
                row.get("attribution"),
            ),
        )

    @staticmethod
    def _parse_datetime(value: str | None) -> str | None:
        """Validate and normalise an ISO-8601 datetime."""
        if not value:
            return None

        datetime_value = datetime.fromisoformat(value)

        if datetime_value.tzinfo is None:
            raise ValueError(
                "captured_at must contain timezone information."
            )

        return datetime_value.isoformat()

    @staticmethod
    def _parse_float(value: str | None) -> float | None:
        """Convert a CSV value to a float, or None if empty."""
        if not value:
            return None

        return float(value)