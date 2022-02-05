# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.
"""

#region Imports
from .utils import sorted_by_key  # noqa
from haversine import haversine
#endregion

#region Functions
def distance(coord, p):
    """Computes geographical distance between two points, used to increase readability over calling haversine directly."""
    return haversine(coord, p)  

### Task 1C
def stations_within_radius(stations, centre, r):
    """Returns a list of stations within radius r of a given co-ordinate.

    Params:
        Stations - List of Stations to be Filtered. \n
        Centre - The coordinate around which the radius is measured. The 'search parameter'. \n
        R - The radius by which the function filters in km.
    """
    result = []
    for i in range(len(stations)):  
        if(haversine(stations[i].coord, centre) < r): # it would never be exactly equal to anyways.
            result.append(stations[i])
    return result

### Task 1B
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

### Task 1D
# list of stations in
# return container with names of rivers with a monitoring station
# should not return duplicates, use set
def rivers_with_station(stations):
    rivers = {} # set
    for station in stations: # iterate and add rivers to set
        rivers += station.river
    return rivers
#endregion