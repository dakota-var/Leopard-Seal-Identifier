import csv
from datetime import date, datetime, timezone

import uuid
from uuid import uuid4
from leopard_id.database.repositories import ObservationRepository as Repo
from leopard_id.ingestion.validation.observations import validate_observation
from leopard_id.ingestion.validation import CommonValidation as ComVal
from leopard_id.models import ObservationModel as Model, ObservationModel

from datetime import date

class INatCSVImport:
    def __init__(self,
                 repository: Repo = Repo,
                 csv_path: str = "observations.csv",
                 ) -> None:
        imported = import_inat_observations(csv_path, repository)
        print(f"\nImported {imported} observations from {csv_path}")

def parse_date(value: str | None) -> date | None:
    if not value:
        return None

    value = value.strip()

    # ISO format: YYYY-MM-DD
    try:
        return date.fromisoformat(value)
    except ValueError:
        pass

    # iNaturalist export format: DD/MM/YYYY
    try:
        return datetime.strptime(value, "%d/%m/%Y").date()
    except ValueError:
        raise ValueError(f"Unrecognised date format: {value!r}")


def parse_datetime(value: str | None) -> datetime | None:
    if not value:
        return None

    value = value.strip()

    if value.endswith(" UTC"):
        value = value[:-4] + "+00:00"

    elif value.endswith("Z"):
        value = value[:-1] + "+00:00"

    return datetime.fromisoformat(value)


def import_inat_observations(csv_path: str, repository: Repo) -> int:
    """Import observations from an iNaturalist CSV file."""

    imported = 0

    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:

            if Repo.uuid_exists(repository, uuid.UUID(row.get("uuid"))):
                prev_update = parse_datetime(repository.get_by_uuid(uuid.UUID(row.get("uuid"))).source_updated_at)
                if prev_update and prev_update >= parse_datetime(row.get("updated_at")):
                    continue


            try:
                observation = Model(
                    ### Database-specific fields
                    database_uuid=uuid4(),
                    source_name="iNaturalist",
                    issues=None,

                    ### iNaturalist 'basic' fields
                    source_id=ComVal.int(row.get("id")),
                    source_uuid=uuid.UUID(row.get("uuid")) if row.get("uuid") else None,
                    source_created_at=parse_datetime(row.get("created_at")),
                    source_updated_at=parse_datetime(row.get("updated_at")),
                    observed_on_str=ComVal.str(row.get("observed_on_string")),
                    observed_on=parse_date(row.get("observed_on")),
                    time_observed=parse_datetime(row.get("time_observed_at")),
                    time_zone=ComVal.str(row.get("time_zone")),
                    inat_user_id=ComVal.int(row.get("user_id")),
                    inat_user_login=ComVal.str(row.get("user_login")),
                    inat_user_name=ComVal.str(row.get("user_name")),
                    inat_quality_grade=ComVal.str(row.get("quality_grade")),
                    license=ComVal.str(row.get("license")),
                    url=ComVal.str(row.get("url")),
                    image_url=ComVal.str(row.get("image_url")),
                    sound_url=ComVal.str(row.get("sound_url")),
                    tag_list=ComVal.str(row.get("tag_list")),
                    description=ComVal.str(row.get("description")),
                    num_id_agree=ComVal.int(row.get("num_identification_agreements")),
                    num_id_disagree=ComVal.int(row.get("num_identification_disagreements")),
                    captive=bool(row.get("captive_cultivated")) if row.get("captive_cultivated") else None,
                    oauth_app_id=ComVal.int(row.get("oauth_application_id")),

                    ### iNaturalist 'geo' fields
                    place_guess=ComVal.str(row.get("place_guess")),
                    latitude=float(row.get("latitude"))
                                if row.get("latitude")
                                else None,
                    longitude=float(row.get("longitude"))
                                if row.get("longitude")
                                else None,
                    positional_accuracy=float(row.get("positional_accuracy"))
                                if row.get("positional_accuracy")
                                else None,
                    private_place_guess=ComVal.str(row.get("private_place_guess"))
                                if row.get("private_latitude")
                                else None,
                    private_longitude=float(row.get("private_longitude"))
                                if row.get("private_longitude")
                                else None,
                    public_pos_accuracy=float(row.get("public_positional_accuracy"))
                                if row.get("public_positional_accuracy")
                                else None,
                    geoprivacy=ComVal.str(row.get("geoprivacy")),
                    taxon_geoprivacy=ComVal.str(row.get("taxon_geoprivacy")),
                    coordinates_obscured=bool(row.get("coordinates_obscured"))
                                if row.get("coordinates_obscured")
                                else None,
                    positioning_method=ComVal.str(row.get("positioning_method")),
                    positioning_device=ComVal.str(row.get("positioning_device")),
                    place_town_name=ComVal.str(row.get("place_town_name")),
                    place_county_name=ComVal.str(row.get("place_county_name")),
                    place_state_name=ComVal.str(row.get("place_state_name")),
                    place_country_name=ComVal.str(row.get("place_country_name")),
                    place_admin1_name=ComVal.str(row.get("place_admin1_name")),
                    place_admin2_name=ComVal.str(row.get("place_admin2_name")),

                    ### iNaturalist 'taxon' fields
                    species_guess=ComVal.str(row.get("species_guess")),
                    scientific_name=ComVal.str(row.get("scientific_name")),
                    common_name=ComVal.str(row.get("common_name")),
                    iconic_taxon_name=ComVal.str(row.get("iconic_taxon_name")),
                    taxon_id=ComVal.int(row.get("taxon_id")),
                )

                issues = validate_observation(observation)
                if issues:
                    raise ValueError(f"Validation errors: {issues}")

                if Repo.uuid_exists(repository, uuid.UUID(row.get("uuid"))):
                    repository.update(uuid.UUID(row.get("uuid")), observation)
                else:
                    repository.add(observation)

                imported += 1
                print(
                    f"\rImported observation {imported}",
                    end="", flush=True
                )

            except ValueError as e:
                print(f"\nError importing observation {imported}: {e}")

    return imported