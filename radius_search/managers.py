from django.db.models.manager import BaseManager

from .querysets import LocationQuerySet


class LocationManager(BaseManager.from_queryset(LocationQuerySet)):
    """
    Manager class for location models constructed from LocationQuerySet.
    Overwrite get_distance_unit for customization.
    """
