from django.db import models

try:
    # Try to import math functions from django core (Django >= 2.2)
    from django.db.models.functions.math import Acos, Cos, Radians, Sin
except ImportError:
    # Import custom math functions as fallback
    from dbfunctions import Acos, Cos, Radians, Sin


class LocationManager(models.Manager):
    """
    Manager class for location models.
    """
    def perimeter(self, mid_point, radius, radius_unit='km', latitude='latitude', longitude='longitude'):
        """
        Returns a query set of locations in a specified radius (using the Haversine formula).
        :param mid_point: middle point of search radius (e.g. tuple of floats)
        :param radius: search radius in km or miles
        :param radius_unit: should be either 'km' (default) or 'miles'
        :param latitude: query selector for latitude field
        :param longitude: query selector for longitude field
        :return: Query set of found locations
        """
        earth_radius = 3959 if radius_unit == 'miles' else 6371
        return self.get_queryset().annotate(distance=(earth_radius * Acos(
            Cos(Radians(latitude)) * Cos(Radians(mid_point[0])) * Cos(Radians(mid_point[1]) - Radians(longitude)) + Sin(
                Radians(latitude)) * Sin(Radians(mid_point[0]))))).filter(distance__lte=radius)
