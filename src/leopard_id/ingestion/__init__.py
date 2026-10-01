"""Data ingestion functionality.

This package contains functionality for importing observations and
associated metadata from external data sources into the application.
"""

from .observations import ObservationsImporter

__all__ = ["ObservationsImporter"]