# System Architecture

## Overview

Leopard Seal Identification & Tracking is designed as a modular research-oriented software system for managing wildlife observations and, eventually, identifying individual leopard seals from photographs.

The system separates data management, machine learning, identification, and user-facing functionality so that each component can be developed and tested independently.

## High-Level Architecture

The planned architecture consists of the following major components:

```text
                    ┌─────────────────────┐
                    │      User / API     │
                    └──────────┬──────────┘
                               │
              ┌────────────────┴────────────────┐
              │                                 │
       ┌──────▼───────┐                 ┌──────▼───────┐
       │ Identification│                 │   Mapping    │
       │    System     │                 │   & Analysis │
       └──────┬────────┘                 └──────┬───────┘
              │                                 │
              └────────────────┬────────────────┘
                               │
                       ┌───────▼───────┐
                       │    Database   │
                       │  & Repository │
                       └───────┬───────┘
                               │
                       ┌───────▼───────┐
                       │ Image / Data  │
                       │    Storage    │
                       └───────────────┘

                 Machine Learning
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       Species        Sex       Individual
    Classification Classification Identification
```

This represents the intended architecture and may change as development progresses.

## Components

### Data Management

Responsible for storing and retrieving:

* Individual seal records
* Photographs and their metadata
* Sightings
* Locations
* Model predictions
* Human reviews
* Model versions

The database stores metadata and relationships rather than the image files themselves.

### Image Ingestion

Responsible for importing photographs into the system and extracting or recording relevant metadata.

Potential metadata includes:

* Image source
* Source identifier
* Capture date and time
* Geographic coordinates
* Species
* Photographer
* Licence information
* File path
* Image checksum

### Machine Learning

The machine-learning system is intended to consist of several stages:

1. Species classification
2. Sex classification
3. Individual identification

Each stage should be independently testable and versioned.

### Individual Identification

Individual identification is expected to use visual similarity rather than a conventional fixed multiclass classifier.

The system should generate a representation (embedding) of the seal's visual characteristics and compare it with known individuals.

This approach is intended to allow the system to recognise previously unseen individuals.

### Human Review

Predictions that do not meet an appropriate confidence threshold should be presented for human review.

Human decisions should be recorded rather than silently replacing the original model prediction.

These decisions can subsequently be incorporated into future training datasets.

### Mapping and Analysis

The system will eventually use sighting locations and timestamps to provide information about:

* Individual movements
* Sightings over time
* Geographic distribution
* Areas of congregation
* Potential changes in distribution

## Data Flow

A typical image-processing workflow is intended to follow this pattern:

```text
Image
  │
  ▼
Ingestion
  │
  ▼
Species Classification
  │
  ├── Not a leopard seal ──► Reject
  │
  ├── Undetermined ─────────► Human Review
  │
  ▼
Sex Classification
  │
  ▼
Individual Identification
  │
  ├── Known individual ─────► Record sighting
  │
  ├── New individual ───────► Create candidate record
  │
  └── Uncertain ────────────► Human Review
                               │
                               ▼
                         Record decision
```

## Design Principles

### Separation of Concerns

Different responsibilities should be kept in separate modules where practical.

### Provenance

Data should retain information about where it came from and how it was processed.

### Human-in-the-Loop

The system should support human verification rather than assuming that machine-learning predictions are always correct.

### Reproducibility

Model versions, processing steps, and data sources should be recorded wherever practical.

### Extensibility

The architecture should allow additional species, models, data sources, and analysis features to be added in the future.

## Current Stage

Stage 1 focuses primarily on the data-management foundation.

Machine-learning components described above represent the planned architecture and are not necessarily implemented yet.
