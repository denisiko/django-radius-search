from radius_search.querysets import LocationQuerySet
from radius_search.settings import DISTANCE_UNIT_MILES


class LocationQuerySet(LocationQuerySet):
    """
    Query set class for location models with miles as distance unit.
    """
    DISTANCE_UNIT = DISTANCE_UNIT_MILES
