# Data Design

## Overview

The project uses photographs, observation metadata, machine-learning predictions, human reviews, and individual seal records.

The data is divided into source data, processed data, and application data.

## Data Categories

### Images

Photographs of leopard seals and other species used by the identification system.

Images should generally be stored outside the Git repository when they are large or numerous.

The application stores a reference to each image rather than storing the image itself in the database.

### Image Metadata

Metadata associated with an image may include:

* Image identifier
* File path or storage reference
* Original source
* Source identifier
* Photographer
* Licence
* Capture date and time
* Latitude
* Longitude
* Species
* File checksum

### Individuals

An individual leopard seal record represents a recognised seal.

A record may contain:

* Unique identifier
* Sex
* First known sighting
* Most recent sighting
* Notes
* Creation timestamp

Individual records should not depend on a particular image filename or external source identifier.

### Sightings

A sighting represents an observation of an individual at a particular time and location.

A sighting may reference:

* Individual seal
* Image
* Observation date and time
* Latitude
* Longitude
* Identification confidence
* Source

Separating sightings from individuals allows one seal to have many observations.

### Predictions

Every machine-learning prediction should be recorded.

A prediction should contain information such as:

* Image
* Model version
* Prediction type
* Predicted value
* Confidence
* Timestamp

Examples of prediction types include:

* Species
* Sex
* Individual identity

The original prediction should remain available even if a human later determines that it was incorrect.

### Human Reviews

Human reviews record decisions made by researchers or other authorised reviewers.

A review may contain:

* Image
* Prediction being reviewed
* Review decision
* Reviewer
* Notes
* Timestamp

Human corrections should be retained as data that can potentially be used for future model development.

## Relationships

The intended relationships between the major entities are:

```text
Individual
    │
    │ 1
    │
    ├──────────< Sightings >────────── Image
    │
    │
    └──────────< Predictions >──────── Image
                                      │
                                      │
                                      ▼
                                    Review
```

One individual can have many sightings.

One image may be associated with a sighting and may have multiple predictions.

A prediction may subsequently be reviewed by a human.

## Database

SQLite will initially be used as the project's database.

The database is intended to contain metadata and relationships rather than large image files.

The initial schema is expected to include tables representing:

* Individuals
* Images
* Sightings
* Predictions
* Reviews

The schema may change as the requirements become clearer.

## Data Storage

The project separates data from application source code.

```text
data/
├── raw/
├── interim/
├── processed/
├── training/
└── test/
```

### `raw/`

Original downloaded or imported data.

Raw data should be treated as immutable wherever possible.

### `interim/`

Temporary data produced during processing.

### `processed/`

Cleaned or transformed data ready for use by the application or machine-learning pipeline.

### `training/`

Data prepared specifically for model training.

### `test/`

A small, controlled dataset used for development and testing.

Large datasets should generally not be committed directly to Git.

## Data Provenance

Externally sourced data must retain information about its origin and applicable licence.

For each image, the project should record provenance information where available.

At minimum, this should include:

* Source
* Source identifier
* Original URL
* Creator
* Licence
* Attribution requirements

The software's MIT licence does not automatically apply to externally sourced photographs or datasets.

See `data/README.md` for dataset-specific provenance and licensing information.

## Data Quality

Data should be validated before being used for training or analysis.

Potential validation checks include:

* Valid image file
* Valid species label
* Valid coordinates
* Valid timestamp
* Valid licence information
* Duplicate detection
* Missing metadata
* Consistent individual identifiers

## Machine-Learning Data Leakage

Care must be taken when creating training, validation, and test datasets.

Multiple photographs of the same individual, particularly photographs from the same encounter, should not automatically be treated as independent observations.

Dataset splitting should prevent information about an individual appearing in both training and evaluation data when doing so would produce an unrealistically optimistic evaluation.

## Future Extensions

The data model may eventually support:

* Multiple species
* Image regions or bounding boxes
* Image segmentation
* Multiple individuals in one photograph
* Geospatial analysis
* Model training runs
* Dataset versions
* Annotation history
* External research datasets
