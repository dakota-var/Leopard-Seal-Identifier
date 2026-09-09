"""Review model for Leopard Seal Identification & Tracking."""

from datetime import datetime


class Review:
    """Represent a human review of a machine-learning prediction."""

    def __init__(
        self,
        review_id: int,
        prediction_id: int,
        decision: str,
        reviewer: str | None = None,
        corrected_prediction: str | None = None,
        notes: str | None = None,
        created_at: datetime | None = None,
    ) -> None:
        self._id = review_id
        self.prediction_id = prediction_id
        self.decision = decision
        self.reviewer = reviewer
        self.corrected_prediction = corrected_prediction
        self.notes = notes
        self.created_at = created_at

    @property
    def id(self) -> int:
        """Return the unique identifier of this review."""
        return self._id