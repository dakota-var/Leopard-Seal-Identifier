"""Database package for Leopard Seal Identification & Tracking.

This package provides the database connection, schema initialisation,
and data-access infrastructure used by the application.
"""

from .database import Database

__all__ = ["Database"]