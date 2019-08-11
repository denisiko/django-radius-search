from django.db.models.manager import BaseManager

from .querysets import LocationQuerySet
from .settings import DISTANCE_UNIT_KM


class LocationManager(BaseManager.from_queryset(LocationQuerySet)):
    """
    Manager class for location models constructed from LocationQuerySet.
    Overwrite with DISTANCE_UNIT as DISTANCE_UNIT_MILES to customize.
    """
    DISTANCE_UNIT = DISTANCE_UNIT_KM

    def get_queryset(self):
        """
        Returns the query set with DISTANCE_UNIT passed into it.
        :return: query set for locations
        """
        queryset = super(LocationManager, self).get_queryset()
        queryset.distance_unit = self.DISTANCE_UNIT
        return queryset
