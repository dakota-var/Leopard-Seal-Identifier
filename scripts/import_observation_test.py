from leopard_id.database.engine import SessionLocal
from leopard_id.database.repositories import ObservationRepository
from leopard_id.ingestion.observations import import_inat_observations


def main() -> None:
    with SessionLocal() as session:
        repository = ObservationRepository(session)

        try:
            imported = import_inat_observations(
                "../data/unit_testing/test_dataset.csv",
                repository,
            )

            session.commit()

        except Exception:
            session.rollback()
            raise

    print(f"Imported {imported} observations.")


if __name__ == "__main__":
    main()