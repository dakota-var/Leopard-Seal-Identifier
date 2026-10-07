package nz.co.dakotav.lepseal.model.observation;

import nz.co.dakotav.lepseal.model.observation.SourceMetadata;
import nz.co.dakotav.lepseal.model.observation.SourceSite;
import nz.co.dakotav.lepseal.model.util.ChangeLog;
import org.junit.jupiter.api.Test;

import java.time.OffsetDateTime;
import java.time.ZoneOffset;
import java.util.List;
import java.util.UUID;


@SuppressWarnings("SpellCheckingInspection")
public class SourceMetadataTest {
    // Example metadata for testing
    SourceSite baseSourceSite = SourceSite.fromName("iNaturalist");
    Integer baseId = 123;
    UUID baseUuid = UUID.fromString("b6ea67f9-d433-4273-804a-5430449e6a50");
    OffsetDateTime baseCreated = OffsetDateTime.of(2020, 12, 30, 12, 0, 0, 0, ZoneOffset.ofHours(0));
    OffsetDateTime baseUpdated = OffsetDateTime.of(2021, 12, 30, 12, 0, 0, 0, ZoneOffset.ofHours(0));
    String baseUrl = "https://www.inaturalist.nz/observations/123";
    String baseImageUrl = "https://static.inaturalist.org/photos/123/square_medium.jpg";
    String baseSoundUrl = "https://static.inaturalist.org/sounds/123.mp3";
    String baseLicense = "CC BY-NC-SA 4.0";
    String baseQualityGrade = "research";


    SourceMetadata testMetadata = new SourceMetadata.Builder(
            baseSourceSite,
            baseId,
            baseUuid,
            baseCreated
    )
            .updatedAt(baseUpdated)
            .url(baseUrl)
            .imageUrl(baseImageUrl)
            .soundUrl(baseSoundUrl)
            .license(baseLicense)
            .qualityGrade(baseQualityGrade)
            .build();

    // ============================================================================================
    // Tests for getters
    // ============================================================================================

    @Test
    public void testGetDbUuid() {
        UUID dbUuid = testMetadata.getDbUuid();
        assert equal(dbUuid, testMetadata.getDbUuid());
    }

    @Test
    public void testGetDbCreatedAt() {
        OffsetDateTime dbCreatedAt = testMetadata.getDbCreatedAt();
        assert equal(dbCreatedAt, testMetadata.getDbCreatedAt());
    }

    @Test
    public void testGetDbUpdatedAt() {
        OffsetDateTime dbUpdatedAt = testMetadata.getDbUpdatedAt();
        assert equal(dbUpdatedAt, testMetadata.getDbUpdatedAt());
    }

    @Test
    public void testGetSite() {
        SourceSite site = testMetadata.getSite();
        assert equal(baseSourceSite, site, testMetadata.getSite());
    }

    @Test
    public void testGetId() {
        Integer id = testMetadata.getId();
        assert equal(baseId, id, testMetadata.getId());
    }

    @Test
    public void testGetUuid() {
        UUID uuid = testMetadata.getUuid();
        assert equal(baseUuid, uuid, testMetadata.getUuid());
    }

    @Test
    public void testGetCreatedAt() {
        OffsetDateTime createdAt = testMetadata.getCreatedAt();
        assert equal(baseCreated, createdAt, testMetadata.getCreatedAt());
    }

    @Test
    public void testGetUpdatedAt() {
        OffsetDateTime updatedAt = testMetadata.getUpdatedAt();
        assert equal(baseUpdated, updatedAt, testMetadata.getUpdatedAt());
    }

    @Test
    public void testGetUrl() {
        String url = testMetadata.getUrl();
        assert equal(baseUrl, url, testMetadata.getUrl());
    }

    @Test
    public void testGetImageUrl() {
        String imageUrl = testMetadata.getImageUrl();
        assert equal(baseImageUrl, imageUrl, testMetadata.getImageUrl());
    }

    @Test
    public void testGetSoundUrl() {
        String soundUrl = testMetadata.getSoundUrl();
        assert equal(baseSoundUrl, soundUrl, testMetadata.getSoundUrl());
    }

    @Test
    public void testGetLicense() {
        String license = testMetadata.getLicense();
        assert equal(baseLicense, license, testMetadata.getLicense());
    }

    @Test
    public void testGetQualityGrade() {
        String qualityGrade = testMetadata.getQualityGrade();
        assert equal(baseQualityGrade, qualityGrade, testMetadata.getQualityGrade());
    }

    // ============================================================================================
    // Test update via Builder
    // ============================================================================================

    @Test
    public void testUpdateViaBuilder() {
        OffsetDateTime old = testMetadata.getDbUpdatedAt();

        SourceMetadata updatedMetadata = new SourceMetadata.Builder(testMetadata)
                .license("All Rights Reserved")
                .build();

        OffsetDateTime newA = testMetadata.getDbUpdatedAt();
        OffsetDateTime newB = updatedMetadata.getDbUpdatedAt();

        assert notEqual(old, newA, newB);
        assert equal(newA, newB);
        assert notEqual(baseLicense, testMetadata.getLicense());
        assert equal("All Rights Reserved", updatedMetadata.getLicense());
        assert equal(baseQualityGrade, updatedMetadata.getQualityGrade());
        assert equal(baseSoundUrl, updatedMetadata.getSoundUrl());
        assert equal(baseImageUrl, updatedMetadata.getImageUrl());
        assert equal(baseUrl, updatedMetadata.getUrl());
        assert equal(baseId, updatedMetadata.getId());
        assert equal(baseUuid, updatedMetadata.getUuid());
        assert equal(baseSourceSite, updatedMetadata.getSite());
        assert equal(baseCreated, updatedMetadata.getCreatedAt());
        assert equal(baseUpdated, updatedMetadata.getUpdatedAt());
        assert equal(baseSourceSite, updatedMetadata.getSite());

    }


    // ============================================================================================
    // Helper methods
    // ============================================================================================

    private static boolean notEqual(Object a, Object b) {
        return !a.equals(b);
    }

    private static boolean notEqual(Object a, Object b, Object c) {
        return !a.equals(b) || !b.equals(c);
    }

    private static boolean equal(Object a, Object b) {
        return a.equals(b);
    }

    private static boolean equal(Object a, Object b, Object c) {
        return a.equals(b) && b.equals(c);
    }
}
