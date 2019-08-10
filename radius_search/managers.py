from django.db.models.manager import BaseManager

from .querysets import LocationQuerySet
from .settings import DISTANCE_UNIT_KM


class LocationManager(BaseManager.from_queryset(LocationQuerySet)):
    """
    Manager class for location models constructed from LocationQuerySet.
    Overwrite with DISTANCE_UNIT as DISTANCE_UNIT_MILES to customise.
    """
    DISTANCE_UNIT = DISTANCE_UNIT_KM