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
    def __init__(self, distance_unit=DISTANCE_UNIT_KM, *args, **kwargs):
        """
        Initializes the query set instance and sets distance_unit.
        :param distance_unit: 'km' (default) or 'mi'
        :param args: other arguments
        :param kwargs: other arguments as keywords
        """
        self.distance_unit = distance_unit
        super(LocationQuerySet, self).__init__(*args, **kwargs)

    def perimeter(self, mid_point, radius, latitude='latitude', longitude='longitude'):
        """
        Returns a query set of locations in a specified radius (using the Haversine formula).
        :param mid_point: middle point coordinates of search radius (e.g. tuple of floats)
        :param radius: search radius in km (default) or miles depending on distance_unit
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

    def get_earth_radius(self):
        """
        Returns the earth radius in km (default) or miles depending on distance_unit.
        :return: Integer value for earth radius
        """
        return dict(EARTH_RADIUS_CHOICES).get(self.distance_unit)
