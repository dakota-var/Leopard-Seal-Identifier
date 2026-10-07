package nz.co.dakotav.lepseal.model;

import nz.co.dakotav.lepseal.model.observation.SourceMetadata;
import nz.co.dakotav.lepseal.model.observation.SourceSite;
import nz.co.dakotav.lepseal.model.util.ChangeLog;
import org.junit.jupiter.api.Test;

import java.time.OffsetDateTime;
import java.time.ZoneOffset;
import java.util.List;
import java.util.UUID;

@SuppressWarnings("SpellCheckingInspection")
public class ObservationTest {
    SourceMetadata sourceMetadata = new SourceMetadata.Builder(SourceSite.fromName("iNaturalist"),
                                                               123,
                                                               UUID.randomUUID(),
                                                               OffsetDateTime.now())
                                    .updatedAt(OffsetDateTime.now())
                                    .url("https://www.inaturalist.nz/observations/123")
                                    .imageUrl("https://static.inaturalist.org/photos/123/square_medium.jpg")
                                    .soundUrl("https://static.inaturalist.org/sounds/123.mp3")
                                    .license("CC BY-NC-SA 4.0")
                                    .qualityGrade("research")
                                    .build();

    OffsetDateTime dtDefault = OffsetDateTime.of(2020, 12, 30, 12, 0, 0, 0, ZoneOffset.ofHours(0));
    Observation testObservation = new Observation.Builder(sourceMetadata)
            .observedOnString("2020-12-30")
            .timeObserved(dtDefault)
            .timeZone("Pacific/Auckland")
            .sourceUserId(123)
            .sourceUserLogin("test_user")
            .sourceUserName("Test User")
            .tags("tag1, tag2")
            .description("This is a test observation.")
            .captive(false)
            .placeGuess("Test Place")
            .latitude(123.456)
            .longitude(-78.901)
            .positionalAccuracy(123.45)
            .locationPrivate(true)
            .townName("Test Town")
            .countyName("Test County")
            .stateName("Test State")
            .countryName("Test Country")
            .admin1Name("Test Admin 1")
            .admin2Name("Test Admin 2")
            .numIdentifiersAgree(10)
            .numIdentifiersDisagree(5)
            .speciesGuess("Test Species")
            .scientificName("Test Scientific Name")
            .commonName("Test Common Name")
            .taxonId(12345)
            .build();

    // ============================================================================================
    // Tests for getters
    // ============================================================================================

    // Database ID
    @Test
    public void testGetters() {
        // Database ID
        UUID dbUuid = testObservation.getDbUuid();
        assert equal(dbUuid, testObservation.getDbUuid()) : "Unexpected dbUuid";

        OffsetDateTime dbCreatedAt = testObservation.getDbCreatedAt();
        assert equal(dbCreatedAt, testObservation.getDbCreatedAt()) : "Unexpected dbCreatedAt";


        // Internal logging & metadata
        List<String> issues = testObservation.getIssues();
        assert equal(issues, testObservation.getIssues()) : "Unexpected issues";
        ChangeLog changeLog = testObservation.getChangeLog();
        assert equal(changeLog, testObservation.getChangeLog()) : "Unexpected changeLog";
        OffsetDateTime dbUpdatedAt = testObservation.getDbUpdatedAt();
        assert equal(dbUpdatedAt, testObservation.getDbUpdatedAt()) : "Unexpected dbUpdatedAt";

        // Observation date/time
        String observedOnString = testObservation.getObservedOnString();
        assert equal("2020-12-30", observedOnString, testObservation.getObservedOnString());

    }


    private static boolean equal(Object a, Object b) {
        return a.equals(b);
    }

    private static boolean equal(Object a, Object b, Object c) {
        return a.equals(b) && b.equals(c);
    }

}
