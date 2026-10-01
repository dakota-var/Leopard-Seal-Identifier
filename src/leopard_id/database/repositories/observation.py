from sqlalchemy import select
from sqlalchemy.orm import Session

from leopard_id.models import ObservationModel as Observation


class ObservationRepository:
    """Provides database operations for observations."""

    def __init__(self, session: Session):
        self._session = session

    def add(self, observation: Observation) -> Observation:
        """Add an observation to the database."""
        self._session.add(observation)
        return observation

    def get_by_uuid(self, uuid: str) -> Observation | None:
        """Retrieve an observation by its iNaturalist UUID."""
        statement = select(Observation).where(
            Observation.database_uuid == uuid
        )

        return self._session.scalar(statement)