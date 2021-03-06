from django.db.models.manager import BaseManager

from .querysets import LocationQuerySet


class LocationManager(BaseManager.from_queryset(LocationQuerySet)):
    """
    Manager class for location models constructed from LocationQuerySet.
    Query results are in km because LocationQuerySet uses it as distance unit by default.
    """
