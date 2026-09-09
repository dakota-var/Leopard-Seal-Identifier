from pathlib import Path


class Image:
    """Represent an individual photograph associated with an observation."""

    def __init__(
        self,
        image_id: int,
        url: str,
        file_path: str | Path | None = None,
        source: str | None = None,
        source_id: str | None = None,
        license: str | None = None,
        attribution: str | None = None,
        seals: list["Seal"] | None = None,
    ) -> None:
        self._id = image_id

        self.url = url
        self.file_path = Path(file_path) if file_path is not None else None

        self.source = source
        self.source_id = source_id

        self.license = license
        self.attribution = attribution

        self.seals = seals if seals is not None else []

    @property
    def id(self) -> int:
        """Return the unique identifier of this image."""
        return self._id

    def add_seal(self, seal: "Seal") -> None:
        """Associate a seal with this image."""
        if seal not in self.seals:
            self.seals.append(seal)