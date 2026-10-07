package nz.co.dakotav.lepseal.model;

import nz.co.dakotav.lepseal.model.observation.SourceMetadata;
import nz.co.dakotav.lepseal.model.observation.SourceSite;
import nz.co.dakotav.lepseal.model.util.ChangeLog;

import java.time.LocalDate;
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

public class Observation {
    // Database ID
    private final UUID dbUuid;
    private final OffsetDateTime dbCreatedAt;

    private SourceMetadata sourceMetadata;
    // Internal logging & metadata
    private final List<String> issues;
    private final ChangeLog changeLog;
    private OffsetDateTime dbUpdatedAt;
    // Observation date/time
    private String observedOnString;
    private LocalDate observedOn;
    private OffsetDateTime timeObserved;
    private String timeZone;
    // User/source metadata
    private Integer sourceUserId;
    private String sourceUserLogin;
    private String sourceUserName;
    private String tags;
    private String description;
    private Boolean captive;
    // Geographic & location metadata
    private String placeGuess;
    private Double latitude;
    private Double longitude;
    private Double positionalAccuracy;
    private Boolean locationPrivate;
    private String townName;
    private String countyName;
    private String stateName;
    private String countryName;
    private String admin1Name;
    private String admin2Name;
    // Taxon / identification metadata
    private Integer numIdentifiersAgree;
    private Integer numIdentifiersDisagree;
    private String speciesGuess;
    private String scientificName;
    private String commonName;
    private Integer taxonId;

    private Observation() {
        this.dbUuid = UUID.randomUUID();
        this.dbCreatedAt = OffsetDateTime.now();
        this.dbUpdatedAt = OffsetDateTime.now();
        this.issues = new ArrayList<>();
        this.changeLog = new ChangeLog();
    }

    // ============================================================================================
    // Getters
    // ============================================================================================
    // Database ID
    public UUID getDbUuid() {
        return dbUuid;
    }

    public OffsetDateTime getDbCreatedAt() {
        return dbCreatedAt;
    }

    public OffsetDateTime getDbUpdatedAt() {
        return dbUpdatedAt;
    }

    // Internal logging & metadata
    public List<String> getIssues() {
        return issues;
    }

    public ChangeLog getChangeLog() {
        return changeLog;
    }

    // Observation date/time
    public String getObservedOnString() {
        return observedOnString;
    }

    public LocalDate getObservedOn() {
        return observedOn;
    }

    public OffsetDateTime getTimeObserved() {
        return timeObserved;
    }

    public String getTimeZone() {
        return timeZone;
    }

    // User/source metadata
    public Integer getSourceUserId() {
        return sourceUserId;
    }

    public String getSourceUserLogin() {
        return sourceUserLogin;
    }

    public String getSourceUserName() {
        return sourceUserName;
    }

    public String getTags() {
        return tags;
    }

    public String getDescription() {
        return description;
    }

    public Boolean getCaptive() {
        return captive;
    }

    // Geographic & location metadata
    public String getPlaceGuess() {
        return placeGuess;
    }

    public Double getLatitude() {
        return latitude;
    }

    public Double getLongitude() {
        return longitude;
    }

    public Double getPositionalAccuracy() {
        return positionalAccuracy;
    }

    public Boolean getLocationPrivate() {
        return locationPrivate;
    }

    public String getTownName() {
        return townName;
    }

    public String getCountyName() {
        return countyName;
    }

    public String getStateName() {
        return stateName;
    }

    public String getCountryName() {
        return countryName;
    }

    public String getAdmin1Name() {
        return admin1Name;
    }

    public String getAdmin2Name() {
        return admin2Name;
    }

    // Taxon / identification metadata
    public Integer getNumIdentifiersAgree() {
        return numIdentifiersAgree;
    }

    public Integer getNumIdentifiersDisagree() {
        return numIdentifiersDisagree;
    }

    public String getSpeciesGuess() {
        return speciesGuess;
    }

    public String getScientificName() {
        return scientificName;
    }

    public String getCommonName() {
        return commonName;
    }

    public Integer getTaxonId() {
        return taxonId;
    }

    public static class Builder {
        private final Observation observation;

        public Builder(Observation observation) {
            this.observation = observation;
            observation.dbUpdatedAt = OffsetDateTime.now();
            observation.changeLog.add("Observation updated.");
        }

        public Builder(SourceMetadata sourceMetadata) {
            observation = new Observation();
            observation.sourceMetadata = sourceMetadata;
            observation.dbUpdatedAt = OffsetDateTime.now();
            observation.changeLog.add("Observation created.");
        }

        // Source / provenance
        public Builder sourceMetadata(SourceMetadata sourceMetadata) {
            observation.sourceMetadata = sourceMetadata;
            return this;
        }

        // Observation date/time
        public Builder observedOnString(String observedOnString) {
            observation.observedOnString = observedOnString;
            return this;
        }

        public Builder observedOn(LocalDate observedOn) {
            observation.observedOn = observedOn;
            return this;
        }

        public Builder timeObserved(OffsetDateTime timeObserved) {
            observation.timeObserved = timeObserved;
            return this;
        }

        public Builder timeZone(String timeZone) {
            observation.timeZone = timeZone;
            return this;
        }

        // User/source metadata
        public Builder sourceUserId(Integer sourceUserId) {
            observation.sourceUserId = sourceUserId;
            return this;
        }

        public Builder sourceUserLogin(String sourceUserLogin) {
            observation.sourceUserLogin = sourceUserLogin;
            return this;
        }

        public Builder sourceUserName(String sourceUserName) {
            observation.sourceUserName = sourceUserName;
            return this;
        }

        public Builder tags(String tags) {
            observation.tags = tags;
            return this;
        }

        public Builder description(String description) {
            observation.description = description;
            return this;
        }

        public Builder captive(Boolean captive) {
            observation.captive = captive;
            return this;
        }

        // Geographic & location metadata
        public Builder placeGuess(String placeGuess) {
            observation.placeGuess = placeGuess;
            return this;
        }

        public Builder latitude(Double latitude) {
            observation.latitude = latitude;
            return this;
        }

        public Builder longitude(Double longitude) {
            observation.longitude = longitude;
            return this;
        }

        public Builder positionalAccuracy(Double positionalAccuracy) {
            observation.positionalAccuracy = positionalAccuracy;
            return this;
        }

        public Builder locationPrivate(Boolean locationPrivate) {
            observation.locationPrivate = locationPrivate;
            return this;
        }

        public Builder townName(String townName) {
            observation.townName = townName;
            return this;
        }

        public Builder countyName(String countyName) {
            observation.countyName = countyName;
            return this;
        }

        public Builder stateName(String stateName) {
            observation.stateName = stateName;
            return this;
        }

        public Builder countryName(String countryName) {
            observation.countryName = countryName;
            return this;
        }

        public Builder admin1Name(String admin1Name) {
            observation.admin1Name = admin1Name;
            return this;
        }

        public Builder admin2Name(String admin2Name) {
            observation.admin2Name = admin2Name;
            return this;
        }

        // Taxon / identification metadata
        public Builder numIdentifiersAgree(Integer numIdentifiersAgree) {
            observation.numIdentifiersAgree = numIdentifiersAgree;
            return this;
        }

        public Builder numIdentifiersDisagree(Integer numIdentifiersDisagree) {
            observation.numIdentifiersDisagree = numIdentifiersDisagree;
            return this;
        }

        public Builder speciesGuess(String speciesGuess) {
            observation.speciesGuess = speciesGuess;
            return this;
        }

        public Builder scientificName(String scientificName) {
            observation.scientificName = scientificName;
            return this;
        }

        public Builder commonName(String commonName) {
            observation.commonName = commonName;
            return this;
        }

        public Builder taxonId(Integer taxonId) {
            observation.taxonId = taxonId;
            return this;
        }

        public Observation build() {
            return observation;
        }
    }

}
