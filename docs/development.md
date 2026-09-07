# Development Guide

## Overview

This document describes the development workflow, project structure, and conventions used by Leopard Seal Identification & Tracking.

The project is currently in Stage 1, focusing on establishing the data-management and software foundations.

## Requirements

The project is primarily developed using Python.

The following tools and libraries are expected to be used as development progresses:

* Python
* SQLite
* NumPy
* pandas
* scikit-learn
* PyTorch
* Pillow
* OpenCV

Additional dependencies may be introduced as required.

## Project Structure

```text
leopard-seal-id/
├── docs/
│   ├── architecture.md
│   ├── data.md
│   └── development.md
├── src/
│   └── leopard_id/
├── tests/
├── scripts/
├── data/
│   ├── raw/
│   ├── interim/
│   ├── processed/
│   ├── training/
│   └── test/
├── models/
├── notebooks/
├── README.md
├── LICENSE
├── CITATION.cff
├── .gitignore
└── .gitattributes
```

## Development Environment

A Python virtual environment should be used for development.

For example:

```bash
python -m venv .venv
```

Activate the environment using the appropriate command for the operating system.

On Windows:

```powershell
.venv\Scripts\activate
```

On Linux/macOS:

```bash
source .venv/bin/activate
```

Dependencies should be installed inside the virtual environment rather than globally.

## Source Code

Application source code belongs under:

```text
src/leopard_id/
```

Tests belong under:

```text
tests/
```

Scripts used to perform repeatable project tasks belong under:

```text
scripts/
```

Jupyter notebooks should generally be used for exploration and experimentation rather than as the primary location for production code.

## Testing

Tests should be added alongside new functionality where practical.

The test suite should eventually cover:

* Database operations
* Data validation
* Image ingestion
* Prediction handling
* Review handling
* Identification logic
* API functionality

Tests should not depend on the complete external dataset.

A small controlled test dataset should be used where image data is required.

## Database Development

The database schema should be treated as part of the application's source code.

Changes to the schema should be deliberate and documented.

Database code should be separated from higher-level application logic so that the database implementation can eventually be changed if necessary.

SQLite is the initial database system. A different database system may be introduced in the future if the project's scale requires it.

## Machine-Learning Development

Machine-learning experiments should be reproducible where practical.

Experiments should record:

* Dataset version
* Model architecture
* Model version
* Hyperparameters
* Training configuration
* Evaluation metrics
* Random seeds where applicable

Trained model files should not be committed to Git unless there is a specific reason to do so.

Large model files should instead be stored using an appropriate external storage system or Git LFS if versioning them through Git becomes necessary.

## Git Workflow

Changes should be committed regularly with clear commit messages.

Commits should represent a coherent change rather than a large collection of unrelated modifications.

For example:

```text
Add initial database schema
Add image metadata model
Implement image repository
Add database tests
```

Generated files, virtual environments, large datasets, and other inappropriate files should not be committed.

See `.gitignore` for the files and directories excluded from version control.

## Documentation

Important architectural or data-model decisions should be documented in `docs/`.

Documentation should be updated when the behaviour or design of the system changes significantly.

The README should provide an overview of the project, while the documentation directory contains more detailed technical information.

## Data and Privacy

Externally sourced data must retain its original licensing and attribution information.

Do not commit private, sensitive, or restricted data to the repository.

Large datasets should generally be stored separately from the Git repository.

## Pull Requests

If the project later involves multiple contributors, pull requests should describe:

* What was changed
* Why it was changed
* How it was tested
* Any relevant limitations or known issues

Changes should be reviewed before being merged into the main branch.

## Current Development Stage

### Stage 1 — Data Management & Project Foundation

Current priorities are:

1. Establish the repository structure.
2. Define the initial database schema.
3. Implement database access.
4. Define image and observation metadata.
5. Establish dataset provenance and licensing practices.
6. Create tests for the data-management layer.

Machine-learning functionality will be developed after the data foundation is sufficiently stable.
