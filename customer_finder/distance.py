"""
    Various methods for calculating distance and (in)sanity checks on their
    inputs.
"""

from math import sin, cos, asin, sqrt, radians
from collections import namedtuple

Coord = namedtuple('Coord', 'lat lon')

EARTH_RADUS_KM = 6371.0


def check_coordinate(coord):
    """
    Ensure coordinate is some 2 length sequence comprised of floats only
    """
    if len(coord) != 2:
        raise ValueError('Coordinates must have 2, and only 2 values')

    if not isinstance(coord[0], float) and not isinstance(coord[0], float):
        raise ValueError(
            'Coordinates must be composed of floating point numbers'
        )


def great_circle_distance(coord_a, coord_b, R=EARTH_RADUS_KM):
    """
    params: coordA - a len 2 tuple of the latitude and longitude

    returns: distance (kms): distance in kilometres between two points
    on the surface of a sphere - Sphere assumed to earth, unless other radius
    is specified
    """
    check_coordinate(coord_a)
    check_coordinate(coord_b)
    pt_a = Coord(radians(coord_a[0]), radians(coord_a[1]))
    pt_b = Coord(radians(coord_b[0]), radians(coord_b[1]))

    delta_lat = pt_b.lat - pt_a.lat
    delta_lon = pt_b.lon - pt_a.lon

    a = (
        sin(delta_lat / 2) ** 2 +
        cos(pt_a.lat) * cos(pt_b.lat) * sin(delta_lon / 2) ** 2
    )
    c = 2 * asin(sqrt(a))

    distance = R * c
    return distance
