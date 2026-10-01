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

    def get_by_uuid(self, source_uuid: UUID) -> ObservationModel | None:
        return self._session.scalar(
            select(ObservationModel).where(
                ObservationModel.source_uuid == source_uuid
            )
        )