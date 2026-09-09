from datetime import datetime

from leopard_id.database.models import Image


class Seal:
    """Represent an individual leopard seal."""

    def __init__(
        self,
        seal_id: int | None = None,
        sex: str | None = None,
        first_seen: datetime | None = None,
        last_seen: datetime | None = None,
        notes: str | None = None,
        created_at: datetime | None = None,
        images: list["Image"] | None = None,
    ) -> None:
        self._id = seal_id

        self.sex = sex
        self.first_seen = first_seen
        self.last_seen = last_seen
        self.notes = notes
        self.created_at = created_at

        self.images = images if images is not None else []

    @property
    def id(self) -> int:
        """Return the unique identifier of this seal."""
        return self._id

    def add_image(self, image: "Image") -> None:
        """Associate an image with this seal."""
        if image not in self.images:
            self.images.append(image)