from django.db.models.manager import BaseManager

from .querysets import LocationQuerySet
from .settings import DISTANCE_UNIT_KM


class LocationManager(BaseManager.from_queryset(LocationQuerySet)):
    """
    Manager class for location models constructed from LocationQuerySet.
    Overwrite with DISTANCE_UNIT as DISTANCE_UNIT_MILES to customise.
    """
    DISTANCE_UNIT = DISTANCE_UNIT_KM

    def get_queryset(self):
        """
        Passes distance_unit to the query set.
        :return: query set for locations
        """
        return super(LocationManager, self).get_queryset(distance_unit=self.DISTANCE_UNIT)
