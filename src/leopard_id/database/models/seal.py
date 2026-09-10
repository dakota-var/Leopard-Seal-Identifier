from datetime import datetime, date

from leopard_id.database.models import Image


class Seal:
    """Represent an individual leopard seal."""

    def __init__(
        self,
        seal_id: int | None = None,
        sex: str | None = None,
        first_seen: date | None = None,
        last_seen: date | None = None,
        notes: str | None = None,
        db_created_at: datetime | None = None,
        db_updated_at: datetime | None = None,
    ) -> None:
        self._id = seal_id
        self._sex = sex
        self._first_seen = first_seen
        self._last_seen = last_seen
        self._notes = notes
        self._db_created_at = db_created_at
        self._db_updated_at = db_updated_at

    ### PROPERTIES

    @property
    def id(self) -> int:
        """Return the unique identifier of this seal."""
        return self._id

    @property
    def sex(self) -> str | None:
        """Return the sex of the seal."""
        return self._sex

    @property
    def first_seen(self) -> date | None:
        """Return when the seal was first seen."""
        return self._first_seen

    @property
    def last_seen(self) -> date | None:
        """Return when the seal was last seen."""
        return self._last_seen

    @property
    def notes(self) -> str | None:
        """Return any notes about the seal."""
        return self._notes

    @property
    def db_created_at(self) -> datetime | None:
        """Return the date the seal was created in the database."""
        return self._db_created_at

    @property
    def db_updated_at(self) -> datetime | None:
        """Return the date the seal was last updated in the database."""
        return self._db_updated_at

    ### SETTERS

    @sex.setter
    def sex(self, value: str | None) -> None:
        """Set the sex of the seal."""
        if value not in ["male", "female", "unknown", None]:
            raise ValueError("Sex is not valid. Must be 'male', 'female', or 'unknown'.")
        self._sex = value

    @first_seen.setter
    def first_seen(self, value: date | None) -> None:
        """Set the date the seal was first seen."""
        if value is not None and not isinstance(value, date):
            raise ValueError("First seen must be a date object.")
        self._first_seen = value

    @last_seen.setter
    def last_seen(self, value: date | None) -> None:
        """Set the date the seal was last seen."""
        if value is not None and not isinstance(value, date):
            raise ValueError("Last seen must be a date object.")
        self._last_seen = value

    @notes.setter
    def notes(self, value: str | None) -> None:
        """Set the notes for the seal."""
        self._notes = value