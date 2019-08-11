from django.db import models

from .settings import DISTANCE_UNIT_KM, EARTH_RADIUS_CHOICES

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
        :param radius: search radius in km (default) or miles depending on get_distance_unit
        :param latitude: query selector for latitude
        :param longitude: query selector for longitude
        :return: Annotated query set of found locations
        """
        earth_radius = dict(EARTH_RADIUS_CHOICES).get(self.get_distance_unit())
        distance = (
            earth_radius
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
    def get_distance_unit():
        """
        Returns the distance unit for search radius results.
        Valid choices are 'km' (default) and 'mi'. Overwrite for customization.
        :return: string value for distance unit
        """
        return DISTANCE_UNIT_KM
