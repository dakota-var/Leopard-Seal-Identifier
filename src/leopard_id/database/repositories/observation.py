from sqlalchemy import select
from sqlalchemy.orm import Session
from uuid import UUID
from leopard_id.models import ObservationModel as Observation, ObservationModel




class ObservationRepository:
    """Provides database operations for observations."""

    def __init__(self, session: Session):
        self._session = session

    def add(self, observation: Observation) -> Observation:
        """Add an observation to the database."""
        self._session.add(observation)
        return observation

    def update(
            self,
            source_uuid: UUID,
            observation: Observation,
    ) -> ObservationModel | None:
        """Update an existing observation identified by its source UUID."""
        existing_observation = self.get_by_uuid(source_uuid)

        if existing_observation is None:
            return None

        for column in ObservationModel.__table__.columns():
            column_name = column.name

            if column.primary_key:
                continue

            if column_name in {
                "database_uuid",
                "database_created_at",
                "source_uuid",
            }:
                continue

            setattr(
                existing_observation,
                column_name,
                getattr(observation, column_name),
            )

        return existing_observation
    
    
    def get_by_uuid(self, source_uuid: UUID) -> ObservationModel | None:
        return self._session.scalar(
            select(ObservationModel).where(
                ObservationModel.source_uuid == source_uuid
            )
        )

    def uuid_exists(self, source_uuid: UUID) -> bool:
        """Check if a UUID exists in the database."""
        return (self._session.scalars(
            select(ObservationModel)
            .where(ObservationModel.source_uuid == source_uuid)
            .exists()
            .select())
            .one())

