# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit


def stations_by_distance(stations, p):

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


def rivers_by_station_number(stations, N):
    """Returns a list of the first N (river name, number of stations) tuples with the greatest number of stations.

    Params:
        stations - list of stations to be filtered \n
        N - number of tuples to show
    """

    # Create empty list
    rivers_N_list = []

    # Loop over each station
    for i in range(len(rivers_with_station)):
        # Create tuple of (river name, number of stations)
        tuple =
        # Add tuple to list

        # Sort list by number of stations
