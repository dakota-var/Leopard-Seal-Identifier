"""Domain models for observations, images, and seals."""

from datetime import date, datetime

from leopard_id.database.models import Image


class Observation:
    """Represent an iNaturalist observation."""

    def __init__(
        self,
        observation_id: int,
        uuid: str | None = None,
        observed_on: date | None = None,
        user_id: int | None = None,
        user_login: str | None = None,
        user_name: str | None = None,
        license: str | None = None,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
        url: str | None = None,
        place_guess: str | None = None,
        latitude: float | None = None,
        longitude: float | None = None,
        positional_accuracy: float | None = None,
        private_place_guess: str | None = None,
        private_latitude: float | None = None,
        private_longitude: float | None = None,
        public_positional_accuracy: float | None = None,
        scientific_name: str | None = None,
        common_name: str | None = None,
        iconic_taxon_name: str | None = None,
        taxon_id: int | None = None,
        images: list["Image"] | None = None,
    ) -> None:
        self._id = observation_id

        self.uuid = uuid
        self.observed_on = observed_on

        self.user_id = user_id
        self.user_login = user_login
        self.user_name = user_name

        self.license = license

        self.created_at = created_at
        self.updated_at = updated_at

        self.url = url

        self.place_guess = place_guess
        self.latitude = latitude
        self.longitude = longitude
        self.positional_accuracy = positional_accuracy

        self.private_place_guess = private_place_guess
        self.private_latitude = private_latitude
        self.private_longitude = private_longitude
        self.public_positional_accuracy = public_positional_accuracy

        self.scientific_name = scientific_name
        self.common_name = common_name
        self.iconic_taxon_name = iconic_taxon_name
        self.taxon_id = taxon_id

        self.images = images if images is not None else []

    @property
    def id(self) -> int:
        """Return the unique iNaturalist observation ID."""
        return self._id

    def add_image(self, image: "Image") -> None:
        """Associate an image with this observation."""
        if image not in self.images:
            self.images.append(image)