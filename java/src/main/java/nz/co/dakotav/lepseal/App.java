package nz.co.dakotav.lepseal;

import nz.co.dakotav.lepseal.database.ObservationRepository;
import nz.co.dakotav.lepseal.ingestion.InaturalistImporter;
import nz.co.dakotav.lepseal.validation.ObservationValidator;

import java.nio.file.Path;

/**
 * The App class serves as the entry point for importing observations from
 * a specified file into an observation repository. The main method processes
 * an input file provided via the command-line arguments and performs the
 * import operation using the InaturalistImporter.
 * <p>
 * The workflow involves:
 * - Initialising an ObservationValidator to validate input observations.
 * - Initialising an ObservationRepository to store the validated observations.
 * - Using the InaturalistImporter to handle the import by combining the
 *   functionalities of validation and repository storage.
 * <p>
 * The class outputs a message to indicate the completion of the import process.
 */
public class App {

    public static void main(String[] args) {
        Path inputFile = Path.of(args[0]);

        ObservationValidator validator = new ObservationValidator();
        ObservationRepository repository = new ObservationRepository();

        InaturalistImporter importer =
                new InaturalistImporter(validator, repository);

        importer.importFile(inputFile);

        System.out.println("Import complete.");
    }
}