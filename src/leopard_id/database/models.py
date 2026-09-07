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

import datetime
from pathlib import Path
from uuid import UUID

from leopard_id.utils import parse_date, parse_datetime


class Seal:
    """Represent an individual leopard seal."""

    def __init__(
            self,
            seal_id: int,
            sex: str | None = None,
            first_seen: datetime.datetime | None = None,
            last_seen: datetime.datetime | None = None,
            estimated_birth: datetime.datetime | None = None,
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
        self._created_at = datetime.datetime.now(datetime.timezone.utc)

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
    def first_seen(self) -> datetime.datetime | None:
        """Return the earliest known sighting of the seal."""
        return self._first_seen

    @property
    def last_seen(self) -> datetime.datetime | None:
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

        return datetime.datetime.now(datetime.timezone.utc).year - self.estimated_birth

    @property
    def notes(self) -> str | None:
        """Return additional notes about the individual."""
        return self._notes

    @property
    def created_at(self) -> datetime.datetime | None:
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
    def first_seen(self, value: datetime.datetime | None) -> None:
        if value is not None:
            if value.tzinfo is None:
                raise ValueError("first_seen must be timezone-aware.")

            value = value.astimezone(datetime.timezone.utc)

        if self._first_seen is not None and value is not None:
            if self._first_seen > value:
                raise ValueError("first_seen must be before or equal to the current value.")

        self._first_seen = value

    @last_seen.setter
    def last_seen(self, value: datetime.datetime | None) -> None:
        if value is not None:
            if value.tzinfo is None:
                raise ValueError("last_seen must be timezone-aware.")

            value = value.astimezone(datetime.timezone.utc)

        if self._last_seen is not None and value is not None:
            if self._last_seen < value:
                raise ValueError("last_seen must be after or equal to the current value.")

        self._last_seen = value

    @estimated_birth.setter
    def estimated_birth(self, value: datetime.datetime | None) -> None:
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
            # ID fields ......................... Reference to iNaturalist CSV
            source: str,                                            # Internal
            file_path: str | Path,                                  # Internal
            image_id: int,                                          # Internal
            source_id: str | int | None = None,                     # Column A
            image_uuid: str | UUID | None = None,                   # Column B

            # Date/time fields
            observed_on: str | datetime.datetime | datetime.date | None = None,       # Column D

            # Attribution & iNat metadata fields
            user_id: int | None = None,                             # Column G
            user_login: str | None = None,                          # Column H
            user_name: str | None = None,                           # Column I
            uploaded_at: str | datetime.datetime | None = None,              # Column J
            updated_at: str | datetime.datetime | None = None,               # Column K
            quality_grade: str | None = None,                       # Column L
            licence: str | None = None,                             # Column M

            # URL fields
            url: str | None = None,                                 # Column N
            image_url: str | None = None,                           # Column O

            # Location fields
            place_guess: str | None = None,
            latitude: float | None = None,                          # Column X
            longitude: float | None = None,                         # Column Y
            positional_accuracy: int | None = None,                 # Column Z

            # Species fields
            scientific_name: str | None = None,                     # Column AK
            common_name: str | None = None,                         # Column AL
            taxon_id: int | None = None,                            # Column AN

    ) -> None:
        """Create an Image instance.

        Args:
            # ID fields
            source: The source of the image, e.g., 'iNaturalist'.
            file_path: The path to the image file.
            image_id: The internal identifier for the image.
            source_id: The identifier the original source used to identify the image.
            image_uuid: The unique identifier for the image.

            # Date/time fields
            observed_on: The date the photograph was taken.

            # Attribution & iNat metadata fields
            user_id: The ID of the user who uploaded the image, if available.
            user_login: The login name of the user who uploaded the image, if available.
            user_name: The full name of the user who uploaded the image, if available.
            uploaded_at: The date and time the image was uploaded to iNaturalist, if available.
            updated_at: The date and time the image was last updated on iNaturalist, if available.
            quality_grade: The quality grade of the image, e.g., 'research'.
            licence: The licence applicable to the image, if available.

            # URL fields
            url: The URL of the original record on iNaturalist, if available.
            image_url: The URL of the original image file, if available.

            # Location & geoprivacy fields
            place_guess: The best guess at the location of the photograph, if available.
            latitude: The latitude of the location of the photograph.
            longitude: The longitude of the location of the photograph.
            positional_accuracy: The accuracy of the location of the photograph, if available.

            # Species fields
            scientific_name: The scientific name of the photograph.
            common_name: The common name of the photograph.
            taxon_id: The taxon ID of the photograph.
        """

        # ID fields
        self._source = source
        self._file_path = Path(file_path)
        self._image_id = image_id
        self._source_id = source_id
        self._image_uuid = image_uuid if image_uuid is not None else uuid.uuid4()

        # Date/time fields
        self._observed_on = parse_date(observed_on)
        self._created_at = datetime.datetime.now(datetime.timezone.utc)

        # Attribution & iNat metadata fields
        self._user_id = user_id
        self._user_login = user_login
        self._user_name = user_name
        self._uploaded_at = parse_datetime(uploaded_at)
        self._updated_at = parse_datetime(updated_at)
        self._quality_grade = quality_grade
        self._licence = licence

        # URL fields
        self._url = url
        self._image_url = image_url

        # Location & geoprivacy fields
        self._place_guess = place_guess
        self._latitude = latitude
        self._longitude = longitude
        self._positional_accuracy = positional_accuracy

        # Species fields
        self._scientific_name = scientific_name
        self._common_name = common_name
        self._taxon_id = taxon_id

    ### ----------| PROPERTIES |----------

    # ID fields
    @property
    def source(self) -> str:
        """Return the source of the image."""
        return self._source

    @property
    def file_path(self) -> Path:
        """Return the path to the image file."""
        return self._file_path

    @property
    def image_id(self) -> int:
        """Return the unique internal identifier for this image."""
        return self._image_id

    @property
    def source_id(self) -> str | None:
        """Return the identifier the original source used to identify the image."""
        return self._source_id

    @property
    def image_uuid(self) -> str:
        """Return a unique identifier for the image."""
        return str(self._image_uuid)

    # Date/time fields
    @property
    def observed_on(self) -> datetime.date:
        """Return the date the photograph was taken."""
        return self._observed_on

    ###############################################################


    @property
    def latitude(self) -> float | None:
        """Return the latitude at which the photograph was taken."""
        return self._latitude

    @property
    def longitude(self) -> float | None:
        """Return the longitude at which the photograph was taken."""
        return self._longitude

    @property
    def licence(self) -> str | None:
        """Return the licence applicable to the image."""
        return self._licence

    @property
    def attribution(self) -> str | None:
        """Return the name of the photographer or source."""
        return self._attribution

    @property
    def created_at(self) -> datetime.datetime | None:
        """Return when the image record was created."""
        return self._created_at

    ### ----------| SETTERS |----------
    @source.setter
    def source(self, value: str) -> None:
        self._source = value

    @file_path.setter
    def file_path(self, value: str) -> None:
        self._file_path = value

    @captured_at.setter
    def captured_at(self, value: datetime.datetime | None) -> None:
        if value is not None:
            if value.tzinfo is None:
                raise ValueError("captured_at must be timezone-aware.")
            value = value.astimezone(datetime.timezone.utc)

        self._captured_at = value

    @latitude.setter
    def latitude(self, value: float | None) -> None:
        if value is not None:
            if not -90 <= value <= 90:
                raise ValueError("Latitude must be between -90 and 90.")
        self._latitude = value

    @longitude.setter
    def longitude(self, value: float | None) -> None:
        if value is not None:
            if not -180 <= value <= 180:
                raise ValueError("Longitude must be between -180 and 180.")
        self._longitude = value

    @licence.setter
    def licence(self, value: str | None) -> None:
        self._licence = value


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
        """
        self._id = sighting_id
        self._seal_id = seal_id
        self._image_id = image_id
        self._confidence = confidence
        self._created_at = datetime.datetime.now(datetime.timezone.utc)

    ### ----------| PROPERTIES |----------

    @property
    def id(self) -> int:
        """Return the unique identifier for this sighting."""
        return self._id

    @property
    def seal_id(self) -> int:
        """Return the unique identifier for the Seal seen."""
        return self._seal_id

    @property
    def image_id(self) -> int:
        """Return the unique identifier for the Image in question."""
        return self._image_id

    @property
    def confidence(self) -> float | None:
        """Return the confidence level of the prediction."""
        if self._confidence is not None:
            if not 0 <= self._confidence <= 1:
                raise ValueError("Confidence must be between 0 and 1.")
        return self._confidence

    @property
    def created_at(self) -> datetime.datetime | None:
        """Return when the sighting record was created."""
        return self._created_at

    ### ----------| SETTERS |----------

    @seal_id.setter
    def seal_id(self, value: int) -> None:
        self._seal_id = value

    @image_id.setter
    def image_id(self, value: int) -> None:
        self._image_id = value

    @confidence.setter
    def confidence(self, value: float | None) -> None:
        if value is not None:
            if not 0 <= value <= 1:
                raise ValueError("Confidence must be between 0 and 1.")
        self._confidence = value

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
        self._created_at = datetime.datetime.now(datetime.timezone.utc)

    ### ----------| PROPERTIES |----------

    @property
    def id(self) -> int:
        """Return the unique identifier for this prediction."""
        return self._id

    @property
    def image_id(self) -> int:
        """Return the unique identifier for the Image in question."""
        return self._image_id

    @property
    def model_version(self) -> str:
        """Return the version of the ML model used to make the prediction."""
        return self._model_version

    @property
    def prediction_type(self) -> str:
        """Return the type of prediction, e.g., 'species', 'age'."""
        return self._prediction_type

    @property
    def prediction(self) -> str | None:
        """Return the actual prediction."""
        return self._prediction

    @property
    def confidence(self) -> float | None:
        """Return the confidence level of the prediction."""
        return self._confidence

    @property
    def notes(self) -> str | None:
        """Return additional notes about the prediction."""
        return self._notes

    @property
    def created_at(self) -> datetime.datetime:
        """Return when the prediction record was created."""
        return self._created_at

    ### ----------| SETTERS |----------

    @notes.setter
    def notes(self, value: str | None) -> None:
        self._notes = value

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
        self._created_at = datetime.datetime.now(datetime.timezone.utc)

    ### ----------| PROPERTIES |----------

    @property
    def id(self) -> int:
        """Return the unique identifier for this review."""
        return self._id

    @property
    def decision(self) -> str:
        """Return the decision made by the reviewer."""
        return self._decision

    @property
    def prediction_id(self) -> int | None:
        """Return the unique identifier for the associated Prediction, if any."""
        return self._prediction_id

    @property
    def image_id(self) -> int | None:
        """Return the unique identifier for the associated Image, if any."""
        return self._image_id

    @property
    def reviewer(self) -> str | None:
        """Return the name of the reviewer."""
        return self._reviewer

    @property
    def notes(self) -> str | None:
        """Return additional notes about the review."""
        return self._notes

    @property
    def created_at(self) -> datetime.datetime:
        """Return when the review record was created."""
        return self._created_at

    ### ----------| SETTERS |----------

    @notes.setter
    def notes(self, value: str | None) -> None:
        self._notes = value
