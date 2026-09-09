"""SQLite database management for Leopard Seal Identification & Tracking."""

import sqlite3
from pathlib import Path
from typing import Any, Iterable, Optional, Sequence, Mapping


class Database:
    """Manage the application's SQLite database.

    The Database class is responsible for:

    - Opening and closing the SQLite connection.
    - Creating the database directory when necessary.
    - Initialising the database schema.
    - Executing SQL statements.
    - Managing transactions.

    The class does not contain application-specific data-access methods.
    Those should be implemented by repository classes.
    """

    def __init__(self, path: str | Path) -> None:
        """Create a Database instance.

        The database connection is not opened until ``connect()`` is
        called. This allows a Database object to be created without
        immediately opening a database connection.

        Args:
            path: Path to the SQLite database file.
        """
        self.path = Path(path)
        self._connection: Optional[sqlite3.Connection] = None

    @property
    def connection(self) -> sqlite3.Connection:
        """Return the active database connection.

        Raises:
            RuntimeError: If the database has not been connected.
        """
        if self._connection is None:
            raise RuntimeError(
                "Database is not connected. Call connect() first."
            )

        return self._connection

    def connect(self) -> None:
        """Open the SQLite database connection.
    
        The parent directory of the database file is created if it does
        not already exist.

        Raises:
            sqlite3.Error: If SQLite cannot open the database.
        """
        if self._connection is not None:
            return

        self.path.parent.mkdir(parents=True, exist_ok=True)

        self._connection = sqlite3.connect(self.path)

        # Return rows that can be accessed by column name as well as index.
        self._connection.row_factory = sqlite3.Row

        # Foreign-key constraints are disabled by default in SQLite,
        # so explicitly enable them for this application.
        self._connection.execute("PRAGMA foreign_keys = ON")

    def close(self) -> None:
        """Close the database connection.

        Calling close() when the database is already closed has no effect.
    """
        if self._connection is not None:
            self._connection.close()
            self._connection = None

    def __enter__(self) -> "Database":
        """Open the database when entering a context manager."""
        self.connect()
        return self

    def __exit__(
        self,
        exc_type: Any,
        exc_value: Any,
        traceback: Any,
    ) -> None:
        """Commit or roll back and close the database.

        If an exception occurred inside the context manager, the current
        transaction is rolled back. Otherwise, it is committed.
        """
        if self._connection is None:
            return

        if exc_type is None:
            self._connection.commit()
        else:
            self._connection.rollback()

        self.close()

    def initialise(self) -> None:
        """Create the application's database schema.

        This method is safe to call multiple times. Existing tables are
        not modified or deleted.
        """
        self.connect()

        self.connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS seals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sex TEXT,
                first_seen TEXT,
                last_seen TEXT,
                notes TEXT,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                images TEXT
            );

            CREATE TABLE IF NOT EXISTS images (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_path TEXT NOT NULL,
                source TEXT,
                source_id TEXT,
                captured_at TEXT,
                latitude REAL,
                longitude REAL,
                licence TEXT,
                attribution TEXT,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS sightings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                seal_id INTEGER NOT NULL,
                image_id INTEGER NOT NULL,
                observed_at TEXT,
                latitude REAL,
                longitude REAL,
                confidence REAL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY (seal_id)
                    REFERENCES seals(id)
                    ON DELETE CASCADE,

                FOREIGN KEY (image_id)
                    REFERENCES images(id)
                    ON DELETE CASCADE
            );

            CREATE TABLE IF NOT EXISTS predictions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                image_id INTEGER NOT NULL,
                model_version TEXT NOT NULL,
                prediction_type TEXT NOT NULL,
                prediction TEXT,
                confidence REAL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY (image_id)
                    REFERENCES images(id)
                    ON DELETE CASCADE
            );

            CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                image_id INTEGER NOT NULL,
                prediction_id INTEGER,
                decision TEXT NOT NULL,
                reviewer TEXT,
                notes TEXT,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY (image_id)
                    REFERENCES images(id)
                    ON DELETE CASCADE,

                FOREIGN KEY (prediction_id)
                    REFERENCES predictions(id)
                    ON DELETE SET NULL
            );

            CREATE INDEX IF NOT EXISTS idx_sightings_seal_id
               ON sightings(seal_id);

            CREATE INDEX IF NOT EXISTS idx_sightings_image_id
                ON sightings(image_id);

            CREATE INDEX IF NOT EXISTS idx_predictions_image_id
                ON predictions(image_id);

            CREATE INDEX IF NOT EXISTS idx_reviews_image_id
                ON reviews(image_id);
            """
        )

        self.connection.commit()

    def execute(
        self,
        sql: str,
        parameters: Iterable[Any] = (),
    ) -> sqlite3.Cursor:
        """Execute a single SQL statement.

        Args:
            sql: SQL statement to execute.
            parameters: Values to bind to the SQL statement.

        Returns:
            The SQLite cursor produced by the operation.

        Raises:
            sqlite3.Error: If SQLite cannot execute the statement.
            RuntimeError: If the database is not connected.
        """
        return self.connection.execute(sql, tuple(parameters))

    def executemany(
        self,
        sql: str,
        parameters: Iterable[Sequence[Any] | Mapping[str, Any]],
    ) -> sqlite3.Cursor:
        """Execute a SQL statement repeatedly.
    
        Args:
            sql: SQL statement to execute.
            parameters: Iterable containing parameter sequences.

        Returns:
            The SQLite cursor produced by the operation.
        """
        return self.connection.executemany(sql, parameters)

    def executescript(self, script: str) -> None:
        """Execute multiple SQL statements.

        Args:
            script: SQL script containing one or more statements.
        """
        self.connection.executescript(script)

    def commit(self) -> None:
        """Commit the current transaction."""
        self.connection.commit()

    def rollback(self) -> None:
        """Roll back the current transaction."""
        self.connection.rollback()

if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[3]
    database_path = project_root / "data" / "leopard_id.db"

    database = Database(database_path)
    database.initialise()
    result = database.execute("PRAGMA integrity_check;").fetchone()
    print(f"Database integrity check: {result[0]}")

    tables = database.execute(
        "SELECT name FROM sqlite_master WHERE type = 'table' ORDER BY name;"
    ).fetchall()

    print("Tables:")
    for table in tables:
        print(f"- {table['name']}")

    database.close()
