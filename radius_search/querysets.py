from django.db import models

from .settings import EARTH_RADIUS_KM

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
    def perimeter(self, mid_point, radius, latitude='latitude', longitude='longitude'):
        """
        Returns a query set of locations in a specified radius (using the Haversine formula).
        :param mid_point: middle point coordinates of search radius (e.g. tuple of floats)
        :param radius: search radius in km (default) or miles
        :param latitude: query selector for latitude
        :param longitude: query selector for longitude
        :return: Annotated query set of found locations
        """
        distance = (
            self.get_earth_radius()
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
    def get_earth_radius():
        """
        Returns the earth radius in km. Overwrite to use miles instead.
        :return: Integer value for earth radius
        """
        return EARTH_RADIUS_KM
