# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit


def stations_by_distance(stations, p):
    """Returns a list of tuples containing stations and their distances from coordinate P.

    Params:
        Stations - List of all stations. \n
        P - The radius by which the function filters in km.
    Returns:
        [(Station 1, Distance 1) ... (Station N, Distance N)]
    """
    # Create empty list
    stations_and_distance = []

    for i in range(len(stations)):
        # Find distance of each station from coordinate p
        distance = haversine(stations[i].coord, p)

        # Create tuple with station & distance
        distance_tuple = (stations[i], distance)

        # Add tuple to list
        stations_and_distance.append(distance_tuple)

    # Sort list by distance
    sorted_by_key(stations_and_distance, 1)

    return stations_and_distance
