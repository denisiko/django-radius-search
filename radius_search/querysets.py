from django.db import models

from .settings import RADIUS_UNIT_KM, RADIUS_UNIT_MILES

try:
    # Import math functions from Django core (Django >= 2.2)
    from django.db.models.functions.math import ACos, Cos, Radians, Sin
except ImportError:
    # Import custom math functions as fallback
    from dbfunctions import ACos, Cos, Radians, Sin


class LocationQuerySet(models.QuerySet):
    """
    Query set class for location models.
    """
    RADIUS_UNIT = RADIUS_UNIT_KM

    def perimeter(self, mid_point, radius, radius_unit=RADIUS_UNIT, latitude='latitude', longitude='longitude'):
        """
        Returns a query set of locations in a specified radius (using the Haversine formula).
        :param mid_point: middle point of search radius (e.g. tuple of floats)
        :param radius: search radius in km or miles
        :param radius_unit: should be either 'km' or 'mi'
        :param latitude: query selector for latitude field
        :param longitude: query selector for longitude field
        :return: Annotated query set of found locations
        """
        distance = (
            self.get_earth_radius(radius_unit)
            * ACos(
                Cos(Radians(latitude))
                * Cos(Radians(mid_point[0]))
                * Cos(Radians(mid_point[1]) - Radians(longitude))
                + Sin(Radians(latitude))
                * Sin(Radians(mid_point[0]))
            )
        )
        return self.annotate(distance=distance).filter(distance__lte=radius)

    @staticmethod
    def get_earth_radius(radius_unit):
        """
        Returns the earth radius in given unit.
        :param radius_unit: distance unit ('km' or 'mi')
        :return: Earth radius if radius_unit is 'km' or 'mi' else None
        """
        if radius_unit == RADIUS_UNIT_KM:
            return 6371
        elif radius_unit == RADIUS_UNIT_MILES:
            return 3959
