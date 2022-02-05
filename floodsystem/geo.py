# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.
"""

# region Imports
from .utils import sorted_by_key  # noqa
from haversine import haversine
# endregion

# region Functions


def distance(coord, p):
    """Computes geographical distance between two points, used to increase readability over calling haversine directly."""
    return haversine(coord, p)

# Task 1C


# Task 1C
def stations_within_radius(stations, centre, r):
    """Returns a list of stations within radius r of a given co-ordinate.

    Params:
        Stations - List of Stations to be Filtered. \n
        Centre - The coordinate around which the radius is measured. The 'search parameter'. \n
        R - The radius by which the function filters in km.
    """
    result = []
    for i in range(len(stations)):
        if(haversine(stations[i].coord, centre) < r):  # it would never be exactly equal to anyways.
            result.append(stations[i])
    return result

# Task 1B


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

    for station in stations:
        # Find distance of each station from coordinate p
        distance = haversine(station.coord, p)

        # Create tuple with station & distance
        distance_tuple = (station, distance)

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

#region Task 1D
### Task 1D i)
def rivers_with_station(stations):
    """Returns a set containing all rivers which have a monitoring station.

    Params:
        Stations - List of all stations. \n.
    Returns:
        {River 1, River 2, ... }
    """
    rivers = set() # set
    for station in stations: # iterate and add rivers to set
        rivers.add(station.river)
    return rivers

### Task 1D ii)
# map river names key to a list of station objects on a river
def stations_by_river(stations):
    """ Returns a dictionary containing rivers along with the names of their monitoring stations.
    Params:
        Stations - List of all stations. \n.
    Returns:
        {River 1 : [Station 1, Station 2], River 2 : [Station 3, Station 4], ... }
    """
# iterate through
# if key exists append to list
# else create key
# or get rivers then append all?
    output = {}

    #for river in rivers_with_station(stations):
    #    output = {river : []}
    #for station in stations:
    #    tmp = output.get(station.river)
    #    tmp.append(station.name)
    #    output.update({station.river, tmp})
    for station in stations: # O(N) instead of O(N^2)
        if((tmp := output.get(station.river)) != None): x = tmp
        else: x = []
        output.update({station.river : [station.name] + x})
        #if(station.river in output.keys()):
        #    output.update({station.river : output.get(station.river) + [station.name]})
        #else:
        #    output.update({station.river : [station.name]})
    return output
#endregion      
        
#endregion
