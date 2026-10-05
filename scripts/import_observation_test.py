from leopard_id.database.engine import SessionLocal
from leopard_id.database.repositories import ObservationRepository
from leopard_id.ingestion.observations import INatCSVImport


def main() -> None:
    with SessionLocal() as session:
        repository = ObservationRepository(session)

        try:
            INatCSVImport(csv_path="../data/unit_testing/observations-778362.csv",
                          repository=repository,
                          )
            session.commit()

        except Exception:
            session.rollback()
            raise

    print(f"\nImport complete.")


if __name__ == "__main__":
    main()
