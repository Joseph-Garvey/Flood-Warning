# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""
    # region Task 1A

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    # Custom '<' operator (method)
    """Returns true if self is earlier in alphabetical order."""

    def __lt__(self, other):
        return self.name < other.name

    # Custom '>' operator (method)
    """Returns true if self is later in alphabetical order."""

    def __gt__(self, other):
        return self.name > other.name
    # endregion

    # region Task 1F
    def typical_range_consistent(self):
        """Checks the typical high/low range data for consistency.

        Returns:
            True if the data is consistent \n
            False if the data is unavailable or inconsistent"""

        # Check if no typical range data is available
        if self.typical_range == None:
            consistency = False

        # Check if the reported typical high range is less than the reported typical low
        elif self.typical_range[1] < self.typical_range[0]:
            consistency = False

        # Otherwise data is consistent
        else:
            consistency = True

        return consistency

    # region Task 2B
    def relative_water_level(self):
        """ returns the latest water level as a fraction of the typical range, i.e. a ratio of 1.0 corresponds to a level at the typical high and a ratio of 0.0 corresponds to a level at the typical low. """

        # Check if water level data is consistent & available
        if self.typical_range_consistent == True:
            rel_level = self.latest_level / self.typical_range

        else:
            rel_level = None

        return rel_level


def inconsistent_typical_range_stations(stations):
    """Returns a list of stations that have inconsistent data

    Parameters:
        Stations - list of MonitoringStations objects"""

    # create an empty list
    incons_stations = []

    # Loop over all station objects in stations list
    for station in stations:

        # Check if station has inconsistent data for typical range
        if station.typical_range_consistent() == False:

            # Add station to list
            incons_stations.append(station)

    return incons_stations
# endregion
