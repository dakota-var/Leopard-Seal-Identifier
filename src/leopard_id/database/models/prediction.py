"""Prediction model for Leopard Seal Identification & Tracking."""

from datetime import datetime


class Prediction:
    """Represent a machine-learning prediction made for an image."""

    def __init__(
        self,
        prediction_id: int,
        image_id: int,
        model_version: str,
        prediction_type: str,
        prediction: str,
        confidence: float,
        created_at: datetime | None = None,
    ) -> None:
        self._id = prediction_id
        self.image_id = image_id
        self.model_version = model_version
        self.prediction_type = prediction_type
        self.prediction = prediction
        self.confidence = confidence
        self.created_at = created_at

    @property
    def id(self) -> int:
        """Return the unique identifier of this prediction."""
        return self._id

    @property
    def confidence(self) -> float:
        return self._confidence

    @confidence.setter
    def confidence(self, value: float) -> None:
        if not 0.0 <= value <= 1.0:
            raise ValueError("Confidence must be between 0 and 1.")

        self._confidence = value