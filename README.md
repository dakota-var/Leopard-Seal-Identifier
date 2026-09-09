# Leopard Seal Identification & Tracking

A research-oriented software project exploring the use of machine learning to identify individual leopard seals from their unique spot patterns, record sightings, and analyse their movements and distribution.

## Data Sources and Variables
#### Basic variables
| Label         | Description                                                                                                              | Datatype           |
|---------------|--------------------------------------------------------------------------------------------------------------------------|--------------------|
| `id`          | Unique, sequential identifier for the observation                                                                        | `int`              |
| `uuid`        | Universally unique identifier for the observation                                                                        | `str \| None`      |
| `observed_on` | Date of the observation (normalised)                                                                                     | `date \| None`     |
| `user_id`     | Unique, sequential identifier for the observer                                                                           | `int \| None`      |
| `user_login`  | Handle / username of the observer                                                                                        | `str \| None`      |
| `user_name`   | Name of the observer (may be a pseudonym)                                                                                | `str \| None`      |
| `license`     | Identifier for the license the observer has chosen. All rights reserved if empty (in which case images are not ingested) | `str \| None`      |
| `created_at`  | Date/time observation was created                                                                                        | `datetime \| None` |
| `updated_at`  | Date/time observation was last updated                                                                                   | `datetime \| None` |
| `url`         | URL of the observation                                                                                                   | `str \| None`      |
| `image_url`   | URL of the image associated with the observation                                                                         | `str \| None`      |
#### Geo variables
| Label                        | Description                                                                                            | Datatype        |
|------------------------------|--------------------------------------------------------------------------------------------------------|-----------------|
| `place_guess`                | Locality information as entered by the observer                                                        | `str \| None`   |
| `latitude`                   | Latitude of the observation                                                                            | `float \| None` |
| `longitude`                  | Longitude of the observation                                                                           | `float \| None` |
| `positional_accuracy`        | Coordinate precision                                                                                   | `float \| None` |
| `private_place_guess`        | Usually empty - Locality information as entered by the observer if obscured                            | `str \| None`   |
| `private_latitude`           | Usually empty - Latitude of the observation if obscured                                                | `float \| None` |
| `private_longitude`          | Usually empty - Longitude of the observation if obscured                                               | `float \| None` |
| `public_positional_accuracy` | Max. horizontal positional uncertainty in meters (includes uncertainty added by obscuration of coords) | `float \| None` |

#### Taxon variables
| Label               | Description                                                    | Datatype        |
|---------------------|----------------------------------------------------------------|-----------------|
| `scientific_name`   | Scientific name of the observed taxon according to iNaturalist | `str \| None`   |
| `common_name`       | Common name of the observed taxon according to iNaturalist     | `str \| None`   |
| `iconic_taxon_name` | Higher-level taxonomic category for the observed taxon         | `str \| None`   |
| `taxon_id`          | Unique, sequential identifier for the observed taxon           | `float \| None` |

## Project Status

**Stage 1: Data Management & Project Foundation**

The first stage establishes the database and data-ingestion infrastructure that will support the machine-learning components developed in later stages.

---

## Stage 1: Data Management

The goal of Stage 1 is to create a reliable foundation for storing and managing the information associated with leopard seal photographs and sightings.

The system will be designed to store:

- Photographs and their metadata
- Species information
- Individual seal records
- Sex, where known
- Date and time of observation
- Geographic location
- Data source and attribution
- Model predictions and confidence scores
- Human verification and corrections

The database will be designed with future machine-learning functionality in mind, while remaining independent of any particular ML implementation.

### Initial Data Flow

```text
Photograph / Observation
          │
          ▼
     Data ingestion
          │
          ▼
     Metadata storage
          │
          ▼
       Database
          │
     ┌────┴────┐
     ▼         ▼
  Images    Sightings
              │
              ▼
       Future ML pipeline
````

---

## Dataset Management

The project will use photographs of leopard seals alongside photographs of other species to develop and evaluate the eventual species-identification model.

Potential sources include publicly available biodiversity datasets such as [iNaturalist](https://www.inaturalist.org/).

Raw image datasets will **not** be stored directly in this Git repository. Instead, the repository will contain dataset metadata, provenance information, and tools for obtaining or reproducing datasets where permitted.

Each image should retain relevant information such as:

* Source
* Source observation ID
* Species
* Photographer/creator
* Licence
* Attribution requirements
* Date and time
* Geographic coordinates
* Local image identifier

This is intended to ensure that the provenance and licensing of training data can be tracked throughout the project.

### Dataset Structure

```text
data/
├── metadata/
│   └── images.csv
│
├── raw/
│   └── [locally stored source images]
│
├── interim/
│   └── [intermediate processing]
│
├── processed/
│   └── [processed datasets]
│
└── test/
    └── [small dataset for development/testing]
```

The `raw`, `interim`, `processed`, and training datasets are not intended to be committed to Git.

---

## Database

The initial database will use **SQLite** to keep development simple and portable.

The database will eventually contain entities representing concepts such as:

```text
Seal
 ├── Individual identity
 ├── Sex
 ├── First/last known sightings
 └── Notes

Image
 ├── File location
 ├── Source
 ├── Metadata
 └── Attribution

Sighting
 ├── Individual
 ├── Image
 ├── Date/time
 └── Location

Prediction
 ├── Image
 ├── Model version
 ├── Prediction
 └── Confidence

Review
 ├── Prediction
 ├── Human decision
 └── Reviewer information
```

The schema will evolve as the requirements of later stages become clearer.

---

## Design Principles

Stage 1 establishes several principles that will remain important throughout the project:

### Data provenance

Every observation and image should be traceable back to its source.

### Separation of data and application code

The repository contains the software required to work with the dataset, rather than relying on the dataset itself being stored in Git.

### Human verification

Model predictions will eventually be treated as predictions rather than unquestionable facts. Human corrections and manual identifications will be retained as valuable labelled data.

### Reproducibility

Dataset versions, processing steps, model versions, and decisions should be recorded wherever practical so that results can be reproduced and compared.

### Extensibility

The database and application architecture should support the addition of machine-learning models, individual identification, manual review, and geographic analysis without requiring the Stage 1 system to be redesigned from scratch.

---

## Planned Development

The project is intended to develop through several stages:

1. **Data management & database foundation** (*Current stage*)
2. **Leopard seal species classification**
3. **Sex classification**
4. **Individual identification using visual similarity and spot patterns**
5. **Human-in-the-loop review and model feedback**
6. **Geographic and temporal visualisation of sightings**
7. **Model evaluation, versioning, and iterative improvement**

The eventual system will follow a pipeline broadly resembling:

```text
Upload photograph
       │
       ▼
Species identification
       │
       ├── Other species ──► Reject
       │
       ├── Undetermined ──► Manual review
       │
       ▼
Leopard seal
       │
       ▼
Sex identification
       │
       ▼
Individual identification
       │
       ├── Existing individual
       │
       ├── Likely new individual
       │
       └── Undetermined ──► Manual review
                              │
                              ▼
                       Verified observation
                              │
                       ┌──────┴──────┐
                       ▼             ▼
                   Database       Training data
```

---

## Technology

The project is initially being developed in Python.

Planned technologies include:

* **Python** :: application and data processing
* **SQLite** :: initial relational database
* **pandas / NumPy** :: data processing
* **scikit-learn** :: conventional ML and evaluation
* **PyTorch** :: deep-learning models
* **OpenCV / Pillow** :: image processing
* **FastAPI** :: eventual application API
* **PostgreSQL/PostGIS** :: potential future database and geospatial backend

Not all technologies are required for Stage 1.

---

## Project Goals

The long-term goal is to develop a machine-learning-assisted research tool that can help researchers:

* Identify individual leopard seals from photographs
* Maintain longitudinal records of known individuals
* Detect previously unidentified individuals
* Record and visualise sightings
* Analyse movements and congregation patterns
* Review and correct model decisions
* Use verified observations to improve future model performance

The system is intended to **assist human researchers rather than replace expert judgement**, particularly when the available photographic evidence is insufficient for confident identification.

---

## Disclaimer

This project is an experimental portfolio/research project and is not currently intended for use as a validated wildlife-monitoring system. Any machine-learning predictions should be independently verified before being used for scientific conclusions or management decisions.
