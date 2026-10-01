import csv
from datetime import date, datetime, timezone

import uuid
from uuid import uuid4
from leopard_id.database.repositories import ObservationRepository as Repo
from leopard_id.models import ObservationModel as Model


from datetime import date


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

            this_uuid = row.get("uuid")

            if this_uuid and repository.get_by_uuid(this_uuid):
                continue

            observation = Model(
                ### Database-specific fields
                database_uuid=uuid4(),
                database_created_at=datetime.now(timezone.utc),
                database_updated_at=datetime.now(timezone.utc),
                source_name="iNaturalist",
                issues=None,

                ### iNaturalist 'basic' fields
                source_id=int(row.get("id")) if row.get("id") else None,
                source_uuid=uuid.UUID(row.get("uuid")) if row.get("uuid") else None,
                source_created_at=parse_datetime(row.get("created_at")),
                source_updated_at=parse_datetime(row.get("updated_at")),
                observed_on_str=row.get("observed_on_string"),
                observed_on=parse_date(row.get("observed_on")),
                time_observed=parse_datetime(row.get("time_observed_at")),
                time_zone=row.get("time_zone"),
                inat_user_id=int(row.get("user_id")) if row.get("user_id") else None,
                inat_user_login=row.get("user_login"),
                inat_user_name=row.get("user_name"),
                inat_quality_grade=row.get("quality_grade"),
                license=row.get("license"),
                url=row.get("url"),
                image_url=row.get("image_url"),
                sound_url=row.get("sound_url"),
                tag_list=row.get("tag_list"),
                description=row.get("description"),
                num_id_agree=int(row.get("num_identification_agreements"))
                            if row.get("num_identification_agreements")
                            else None,
                num_id_disagree=int(row.get("num_identification_disagreements"))
                            if row.get("num_identification_disagreements")
                            else None,
                captive=bool(row.get("captive_cultivated")) if row.get("captive_cultivated") else None,
                oauth_app_id=int(row.get("oauth_application_id"))
                            if row.get("oauth_application_id")
                            else None,

                ### iNaturalist 'geo' fields
                place_guess=row.get("place_guess"),
                latitude=float(row.get("latitude"))
                            if row.get("latitude")
                            else None,
                longitude=float(row.get("longitude"))
                            if row.get("longitude")
                            else None,
                positional_accuracy=float(row.get("positional_accuracy"))
                            if row.get("positional_accuracy")
                            else None,
                private_place_guess=row.get("private_place_guess"),
                private_latitude=float(row.get("private_latitude"))
                            if row.get("private_latitude")
                            else None,
                private_longitude=float(row.get("private_longitude"))
                            if row.get("private_longitude")
                            else None,
                public_pos_accuracy=float(row.get("public_positional_accuracy"))
                            if row.get("public_positional_accuracy")
                            else None,
                geoprivacy=row.get("geoprivacy"),
                taxon_geoprivacy=row.get("taxon_geoprivacy"),
                coordinates_obscured=bool(row.get("coordinates_obscured"))
                            if row.get("coordinates_obscured")
                            else None,
                positioning_method=row.get("positioning_method"),
                positioning_device=row.get("positioning_device"),
                place_town_name=row.get("place_town_name"),
                place_county_name=row.get("place_county_name"),
                place_state_name=row.get("place_state_name"),
                place_country_name=row.get("place_country_name"),
                place_admin1_name=row.get("place_admin1_name"),
                place_admin2_name=row.get("place_admin2_name"),

                ### iNaturalist 'taxon' fields
                species_guess=row.get("species_guess"),
                scientific_name=row.get("scientific_name"),
                common_name=row.get("common_name"),
                iconic_taxon_name=row.get("iconic_taxon_name"),
                taxon_id=int(row.get("taxon_id"))
                            if row.get("taxon_id")
                            else None,
            )

            repository.add(observation)
            imported += 1

    return imported
