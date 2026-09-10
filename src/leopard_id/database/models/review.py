"""Review model for Leopard Seal Identification & Tracking."""

from datetime import datetime


class Review:
    """Represent a human review of a machine-learning prediction."""

    def __init__(
        self,
        review_id: int,
        image_id: int,
        prediction_id: int,
        decision: str,
        reviewer: str | None = None,
        corrected_prediction: str | None = None,
        notes: str | None = None,
        db_created_at: datetime | None = None,
    ) -> None:
        self._id = review_id
        self._image_id = image_id
        self._prediction_id = prediction_id
        self._decision = decision
        self._reviewer = reviewer
        self._corrected_prediction = corrected_prediction
        self._notes = notes
        self._db_created_at = db_created_at

    ### PROPERTIES

    @property
    def id(self) -> int:
        """Return the unique identifier of this review."""
        return self._id

    @property
    def image_id(self) -> int:
        """Return the ID of the image this review belongs to."""
        return self._image_id

    @property
    def prediction_id(self) -> int:
        """Return the ID of the prediction being reviewed."""
        return self._prediction_id

    @property
    def decision(self) -> str:
        """Return the review decision."""
        return self._decision

    @property
    def reviewer(self) -> str | None:
        """Return the reviewer name or identifier."""
        return self._reviewer

    @property
    def corrected_prediction(self) -> str | None:
        """Return the corrected prediction, if one was provided."""
        return self._corrected_prediction

    @property
    def notes(self) -> str | None:
        """Return any notes about the review."""
        return self._notes

    @property
    def db_created_at(self) -> datetime | None:
        """Return the date the review was created in the database."""
        return self._db_created_at

    ### SETTERS

    @image_id.setter
    def image_id(self, value: int) -> None:
        """Set the ID of the image this review belongs to."""
        if not isinstance(value, int):
            raise ValueError("Image ID must be an integer.")
        self._image_id = value

    @prediction_id.setter
    def prediction_id(self, value: int) -> None:
        """Set the ID of the prediction being reviewed."""
        if not isinstance(value, int):
            raise ValueError("Prediction ID must be an integer.")
        self._prediction_id = value

    @decision.setter
    def decision(self, value: str) -> None:
        """Set the review decision."""
        if not isinstance(value, str) or not value:
            raise ValueError("Decision must be a non-empty string.")
        self._decision = value

    @reviewer.setter
    def reviewer(self, value: str | None) -> None:
        """Set the reviewer name or identifier."""
        if value is not None and not isinstance(value, str):
            raise ValueError("Reviewer must be a string or None.")
        self._reviewer = value

    @corrected_prediction.setter
    def corrected_prediction(self, value: str | None) -> None:
        """Set the corrected prediction."""
        if value is not None and not isinstance(value, str):
            raise ValueError("Corrected prediction must be a string or None.")
        self._corrected_prediction = value

    @notes.setter
    def notes(self, value: str | None) -> None:
        """Set the notes for the review."""
        if value is not None and not isinstance(value, str):
            raise ValueError("Notes must be a string or None.")
        self._notes = value