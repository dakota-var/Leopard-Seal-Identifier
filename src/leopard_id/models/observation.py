"""
Defines the SQLAlchemy database model for observations.

This module describes how observations are represented within the relational
database, including tables, columns, constraints, indexes, and relationships
required by SQLAlchemy.

The model in this module is persistence-specific and must not be exposed to
application packages outside the database implementation. The corresponding
domain object in ``domain.observation`` represents the application-level concept
of an observation.
"""

from datetime import date, datetime, timezone

import uuid
from sqlalchemy import String, Integer, Boolean, Float, Date, DateTime, BigInteger, UUID
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class ObservationModel(Base):
    """
    SQLAlchemy representation of an observation in the ``observations`` table.

    This class represents the persistence layer's view of an observation. It should
    be converted to and from the application-level
    :class:`leopard_id.domain.observation.Observation` object by the repository layer.
    """

    __tablename__ = "observations"

    # Database-specific fields
    database_id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )
    database_uuid: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        unique=True,
        default=lambda: str(uuid.uuid4())
    )
    database_created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=lambda: datetime.now(timezone.utc)
    )
    database_updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )
    source_name: Mapped[str] = mapped_column(
        String,
        nullable=False
    )
    issues: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )

    # iNaturalist 'basic' fields
    source_id: Mapped[int | None] = mapped_column(
        BigInteger,
        nullable=True,
    )
    source_uuid: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        unique=True,
        nullable=True,
    )
    source_created_at: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )
    source_updated_at: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )
    observed_on_str: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )
    observed_on: Mapped[date | None] = mapped_column(
        Date,
        nullable=True
    )
    time_observed: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )
    time_zone: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )
    inat_user_id: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )
    inat_user_login: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )
    inat_user_name: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )
    inat_quality_grade: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )
    license: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )
    url: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )
    image_url: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )
    sound_url: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )
    tag_list: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )
    description: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )
    num_id_agree: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )
    num_id_disagree: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )
    captive: Mapped[bool | None] = mapped_column(
        Boolean,
        nullable=True
    )
    oauth_app_id: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    # iNaturalist 'geo' fields
    place_guess: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )
    latitude: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )
    longitude: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )
    positional_accuracy: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )
    private_place_guess: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )
    private_latitude: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )
    private_longitude: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )
    public_pos_accuracy: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )
    geoprivacy: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )
    taxon_geoprivacy: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )
    coordinates_obscured: Mapped[bool | None] = mapped_column(
        Boolean,
        nullable=True
    )
    positioning_method: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )
    positioning_device: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )
    place_town_name: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )
    place_county_name: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )
    place_state_name: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )
    place_country_name: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )
    place_admin1_name: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )
    place_admin2_name: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )

    # iNaturalist 'taxon' fields
    species_guess: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )
    scientific_name: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )
    common_name: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )
    iconic_taxon_name: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )
    taxon_id: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )
