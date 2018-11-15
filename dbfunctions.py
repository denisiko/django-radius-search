from django.db.models import Func


class Radians(Func):
    """
    SQL function for converting degrees to radians.
    """
    function = 'RADIANS'
    name = 'Radians'


class Sin(Func):
    """
    SQL function for calculating the sine.
    """
    function = 'SIN'
    name = 'Sin'


class Cos(Func):
    """
    SQL function for calculating the cosine.
    """
    function = 'COS'
    name = 'Cos'


class Acos(Func):
    """
    SQL function for calculating the arccosine.
    """
    function = 'ACOS'
    name = 'Acos'
