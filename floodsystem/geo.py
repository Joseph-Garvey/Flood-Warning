# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit

# Task 1B


def stations_by_distance(stations, p):

    # Create empty list
    stations_and_distance = []

    for station in stations:
        # Find distance of each station from coordinate p
        distance = haversine(stations.coord, p)

        # Create tuple with station & distance
        distance_tuple = (stations, distance)

        # Add tuple to list
        stations_and_distance.append(distance_tuple)

    # Sort list by distance
    sorted_by_key(stations_and_distance, 1)

    return stations_and_distance

# Task 1E


def rivers_by_station_number(stations, N):
    """Returns a list of the first N (river name, number of stations) tuples with the greatest number of stations.

    Params:
        stations - list of stations to be filtered \n
        N - number of tuples to show \n
        Pulls river name & list of stations by river from the dictionary stations_by_river
    """

    # Create empty list
    rivers_n_list = []

    # Loop over each station
    for i in stations_by_river:

        # Create tuple of (river name, number of stations)
        river_n_tuple = (i, len(stations_by_river[i]))

        # Add tuple to list
        rivers_n_list.append(river_n_tuple)

    # Sort list by number of stations
    sorted_list = sorted_by_key(rivers_n_list, 1, True)

    # Slice list for first N
    first_N_rivers = sorted_list[:N]

    # Loop over rest of list
    for i in range(N, len(sorted_list)):

        # check if number of stations is the same as number of stations in Nth river
        if sorted_list[i][1] == first_N_rivers[N - 1][1]:

            # append tuple to sorted list
            first_N_rivers.append(sorted_list[i])

    return first_N_rivers
