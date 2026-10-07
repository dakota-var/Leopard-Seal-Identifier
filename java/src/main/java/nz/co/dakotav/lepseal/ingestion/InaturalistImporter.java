package nz.co.dakotav.lepseal.ingestion;

import java.nio.file.Path;
import nz.co.dakotav.lepseal.database.ObservationRepository;
import nz.co.dakotav.lepseal.validation.ObservationValidator;

public class InaturalistImporter {
    private final ObservationValidator validator;
    private final ObservationRepository repository;

    public InaturalistImporter(ObservationValidator validator, ObservationRepository repository) {
        this.validator = validator;
        this.repository = repository;
    }

    public void importFile(Path inputFile) {

    }
}
