# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit


def distance(coord, p): # increase readability
    return haversine(coord, p)
    
### Task 1C
# return list of all stations within rad r of a geo coord x
# remember distance between two geo points is computed by haversine
def stations_within_radius(stations, centre, r):
    result = []
    for i in range(len(stations)):
        if(haversine(stations[i].coord, centre) < r): # it would never be equal to. these are floats.
            result.append(stations[i])

