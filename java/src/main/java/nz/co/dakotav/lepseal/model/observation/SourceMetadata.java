package nz.co.dakotav.lepseal.model.observation;

import java.time.OffsetDateTime;
import java.util.Objects;
import java.util.UUID;

public class SourceMetadata {
    // Internal metadata
    private final UUID dbUuid;
    private final OffsetDateTime dbCreatedAt;
    private OffsetDateTime dbUpdatedAt;

    // Source metadata
    private final SourceSite site;
    private final Integer id;
    private final UUID uuid;
    private final OffsetDateTime createdAt;
    private OffsetDateTime updatedAt;
    private String url;
    private String imageUrl;
    private String soundUrl;
    private String license;
    private String qualityGrade;


    private SourceMetadata(SourceSite site, Integer id, UUID uuid, OffsetDateTime createdAt) {
        this.dbUuid = UUID.randomUUID();
        this.dbCreatedAt = OffsetDateTime.now();
        this.dbUpdatedAt = OffsetDateTime.now();

        this.site = site;
        this.id = id;
        this.uuid = uuid;
        this.createdAt = createdAt;
    }

    // ============================================================================================
    // Getters
    // ============================================================================================

    // Internal metadata

    public UUID getDbUuid() {
        return dbUuid;
    }
    public OffsetDateTime getDbCreatedAt() {
        return dbCreatedAt;
    }
    public OffsetDateTime getDbUpdatedAt() {
        return dbUpdatedAt;
    }

    // Source metadata

    public SourceSite getSite() {
        return site;
    }
    public Integer getId() {
        return id;
    }
    public UUID getUuid() {
        return uuid;
    }
    public OffsetDateTime getCreatedAt() {
        return createdAt;
    }
    public OffsetDateTime getUpdatedAt() {
        return updatedAt;
    }
    public String getUrl() {
        return url;
    }
    public String getImageUrl() {
        return imageUrl;
    }
    public String getSoundUrl() {
        return soundUrl;
    }
    public String getLicense() {
        return license;
    }
    public String getQualityGrade() {
        return qualityGrade;
    }

    // ============================================================================================
    // Setters
    // ============================================================================================

    public void setUpdatedAt(OffsetDateTime updatedAt) {
        if (this.updatedAt != null && updatedAt.isBefore(this.updatedAt)) {
            throw new IllegalArgumentException("Invalid updatedAt: " + updatedAt);
        }
        this.updatedAt = Objects.requireNonNull(updatedAt);
    }
    public void setUrl(String url) {
        this.url = Objects.requireNonNull(url);
    }
    public void setImageUrl(String imageUrl) {
        this.imageUrl = Objects.requireNonNull(imageUrl);
    }
    public void setSoundUrl(String soundUrl) {
        this.soundUrl = Objects.requireNonNull(soundUrl);
    }
    public void setLicense(String license) {
        this.license = Objects.requireNonNull(license);
    }
    public void setQualityGrade(String qualityGrade) {
        this.qualityGrade = Objects.requireNonNull(qualityGrade);
    }

    // ============================================================================================
    // Builder
    // ============================================================================================

    public static class Builder {
        private final SourceMetadata sourceMetadata;

        public Builder(SourceMetadata sourceMetadata) {
            this.sourceMetadata = sourceMetadata;
            sourceMetadata.dbUpdatedAt = OffsetDateTime.now();
        }

        public Builder(SourceSite sourceSite, Integer id, UUID uuid, OffsetDateTime createdAt) {
            sourceMetadata = new SourceMetadata(sourceSite, id, uuid, createdAt);
            sourceMetadata.dbUpdatedAt = OffsetDateTime.now();
        }

        public Builder updatedAt(OffsetDateTime updatedAt) {
            sourceMetadata.setUpdatedAt(updatedAt);
            return this;
        }

        public Builder url(String url) {
            sourceMetadata.setUrl(url);
            return this;
        }

        public Builder imageUrl(String imageUrl) {
            sourceMetadata.setImageUrl(imageUrl);
            return this;
        }

        public Builder soundUrl(String soundUrl) {
            sourceMetadata.setSoundUrl(soundUrl);
            return this;
        }

        public Builder license(String license) {
            sourceMetadata.setLicense(license);
            return this;
        }

        public Builder qualityGrade(String qualityGrade) {
            sourceMetadata.setQualityGrade(qualityGrade);
            return this;
        }

        public SourceMetadata build() {
            return sourceMetadata;
        }
    }
}
