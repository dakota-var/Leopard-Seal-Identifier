"""
This module provides classes to model entities related to leopard seal tracking,
including their sightings, associated images, predictions, and reviews.

The module defines the following main classes:
- Seal: Represents an individual leopard seal.
- Image: Represents an image associated with a seal.
- Sighting: Represents a recorded sighting of a seal.
- Prediction: Represents predictive data for a seal.
- Review: Represents a review process for a seal-related entry.
"""

from datetime import datetime, timezone

class Seal:
    """Represent an individual leopard seal."""

    def __init__(
            self,
            seal_id: int,
            sex: str | None = None,
            first_seen: datetime | None = None,
            last_seen: datetime | None = None,
            estimated_birth: datetime | None = None,
            notes: str | None = None,
    ) -> None:
        """Create a Seal instance.

        Args:
            seal_id: The unique identifier for this individual seal.
            sex: The known sex of the seal, or None if unknown.
            first_seen: The earliest known sighting of the seal.
            last_seen: The most recent known sighting of the seal.
            estimated_birth: The estimated birth year of the seal, or None if unknown.
            notes: Additional notes about the individual.
        """
        self._id = seal_id
        self._sex = sex
        self._first_seen = first_seen
        self._last_seen = last_seen
        self._estimated_birth = estimated_birth
        self._notes = notes
        self._created_at = datetime.now(timezone.utc)

    ### ----------| PROPERTIES |----------

    @property
    def id(self) -> int:
        """Return the unique identifier for this individual seal."""
        return self._id

    @property
    def sex(self) -> str | None:
        """Return the sex of the seal, or None if unknown."""
        return self._sex

    @property
    def first_seen(self) -> datetime | None:
        """Return the earliest known sighting of the seal."""
        return self._first_seen

    @property
    def last_seen(self) -> datetime | None:
        """Return the most recent known sighting of the seal."""
        return self._last_seen

    @property
    def estimated_birth(self) -> int | None:
        """
        Return the estimated birth year of the seal, or None if unknown.
        The seal's age is calculated from this date.
        """
        return self._estimated_birth

    @property
    def age(self) -> int | None:
        """Return the estimated age of the seal, or None if unknown."""
        if self.estimated_birth is None:
            return None

        return datetime.now(timezone.utc).year - self.estimated_birth

    @property
    def notes(self) -> str | None:
        """Return additional notes about the individual."""
        return self._notes

    @property
    def created_at(self) -> datetime | None:
        """Return when the seal record was created."""
        return self._created_at




    ### ----------| SETTERS |----------

    @sex.setter
    def sex(self, value: str | None) -> None:
        value = value.lower()

        if value not in ("male", "female", None):
            if value.startswith("m"):
                value = "male"
            elif value.startswith("f"):
                value = "female"
            elif value.startswith("u"):
                value = None
            else:
                raise ValueError("Sex must be 'male', 'female', or None.")

        self._sex = value

    @first_seen.setter
    def first_seen(self, value: datetime | None) -> None:
        if value is not None:
            if value.tzinfo is None:
                raise ValueError("first_seen must be timezone-aware.")

            value = value.astimezone(timezone.utc)

        if self._first_seen is not None and value is not None:
            if self._first_seen > value:
                raise ValueError("first_seen must be before or equal to the current value.")

        self._first_seen = value

    @last_seen.setter
    def last_seen(self, value: datetime | None) -> None:
        if value is not None:
            if value.tzinfo is None:
                raise ValueError("last_seen must be timezone-aware.")

            value = value.astimezone(timezone.utc)

        if self._last_seen is not None and value is not None:
            if self._last_seen < value:
                raise ValueError("last_seen must be after or equal to the current value.")

        self._last_seen = value

    @estimated_birth.setter
    def estimated_birth(self, value: datetime | None) -> None:
        if value is not None:
            self._estimated_birth = value.year

    @notes.setter
    def notes(self, value: str | None) -> None:
        self._notes = value

class Image:
    """
    An Image represents a particular photograph/file,
    regardless of whether the seal(s) in it has/have been identified.
    """

    def __init__(
            self,
            image_id: int,
            file_path: str | None = None,
            source: str | None = None,
            source_id: str | None = None,
            captured_at: datetime | None = None,
            latitude: float | None = None,
            longitude: float | None = None,
            licence: str | None = None,
            attribution: str | None = None,
    ) -> None:
        """Create an Image instance.

        Args:
            image_id: The unique identifier for this image.
            file_path: The path to the image file.
            source: The source of the image, e.g., 'iNaturalist', 'Researcher upload'.
            source_id: The identifier the original source used to identify the image.
            captured_at: When the photograph was taken.
            latitude: The latitude at which the photograph was taken.
            longitude: The longitude at which the photograph was taken.
            licence: The licence applicable to the image, e.g., 'CC BY-NC-SA 4.0'.
            attribution: The name of the photographer or source.
        """
        self._id = image_id
        self._file_path = file_path
        self._source = source
        self._source_id = source_id
        self._captured_at = captured_at
        self._latitude = latitude
        self._longitude = longitude
        self._licence = licence
        self._attribution = attribution
        self._created_at = datetime.now(timezone.utc)


class Sighting:
    """
    A sighting is a record of a seal being seen in a particular location.
    It connects a Seal to an Image.
    """
    def __init__(
            self,
            sighting_id: int,
            seal_id: int,
            image_id: int,
            confidence: float | None = None,
    ) -> None:
        """Create a Sighting instance.

        Args:
            sighting_id: The unique identifier for this sighting.
            seal_id: The unique identifier for the Seal seen.
            image_id: The unique identifier for the Image in question.
            confidence: The confidence level of the prediction.
            created_at: When the sighting record was created.
        """
        self._id = sighting_id
        self._seal_id = seal_id
        self._image_id = image_id
        self._confidence = confidence
        self._created_at = datetime.now(timezone.utc)


class Prediction:
    """
    A Prediction records what an ML model predicts about a Seal.
    Note that this should be preserved even if a reviewer later rejects the prediction.
    """
    def __init__(
            self,
            prediction_id: int,
            image_id: int,
            model_version: str,
            prediction_type: str,
            prediction: str | None = None,
            confidence: float | None = None,
            notes: str | None = None,
    ) -> None:
        """Create a Prediction instance.

        Args:
            prediction_id: The unique identifier for this prediction.
            image_id: The unique identifier for the Image in question.
            model_version: The version of the ML model used to make the prediction.
            prediction_type: The type of prediction, e.g., 'species', 'age'.
            prediction: The actual prediction.
            confidence: The confidence level of the prediction.
            notes: Additional notes about the prediction.
        """

        self._id = prediction_id
        self._image_id = image_id
        self._model_version = model_version
        self._prediction_type = prediction_type
        self._prediction = prediction
        self._confidence = confidence
        self._notes = notes
        self._created_at = datetime.now(timezone.utc)

class Review:
    """
    A Review represents a human evaluation of a Prediction or Image.
    """

    def __init__(
            self,
            review_id: int,
            decision: str,
            prediction_id: int | None = None,
            image_id: int | None = None,
            reviewer: str | None = None,
            notes: str | None = None,
    ) -> None:
        """Create a Review instance."""
        self._id = review_id
        self._decision = decision
        self._prediction_id = prediction_id
        self._image_id = image_id
        self._reviewer = reviewer
        self._notes = notes
        self._created_at = datetime.now(timezone.utc)

