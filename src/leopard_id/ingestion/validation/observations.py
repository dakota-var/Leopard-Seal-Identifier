from leopard_id.models import ObservationModel

from .common import (
    validate_date,
    validate_datetime,
    validate_latitude,
    validate_longitude,
)

__all__ = [
    "validate_observation"
]

def validate_observation(
    observation: ObservationModel,
) -> list[str]:
    issues: list[str] = []

    issues.extend(validate_latitude(observation.latitude))
    issues.extend(validate_longitude(observation.longitude))
    issues.extend(validate_date(observation.observed_on))
    issues.extend(validate_datetime(observation.source_created_at))
    issues.extend(validate_datetime(observation.source_updated_at))
    issues.extend(validate_datetime(observation.time_observed))

    return issues