# region imports
from .station import MonitoringStation
# endregion

# region Task 2B
def stations_level_over_threshold(stations, tol):
    """returns a list of tuples, where each tuple holds (i) a station (object) at which the latest relative water level is over tol and (ii) the relative water level at the station. The returned list should be sorted by the relative level in descending order

    Parameters:
        stations = list of MonitoringStation objects with updated water levels
        tol = tolerance of relative water level shown in final list (float)

    Returns:
        list of [station (MonitoringStation), relative_water_level (float)] tuples"""

    # create empty list
    over_threshold_list = []

    # Loop over all station objects in stations list
    for station in stations:

        # Check if station has relative water level above tol
        if (station.relative_water_level() != None) and (station.relative_water_level() > tol):
            # Create tuple
            over_threshold_tuple = [station, station.relative_water_level()]

            # Add tuple to list
            over_threshold_list.append(over_threshold_tuple)

    # sort list by the relative level in descending order
    over_threshold_list.sort(key=lambda x: x[1], reverse=True)

    return over_threshold_list

# endregion

# region Task 2C
def stations_highest_rel_level(stations, N):
    """Returns a list of the N station objects at which relative water level is highest, sorted in descending order by relative level

    Parameters:
        stations = list of MonitoringStation objects with updated water levels \n
        N = integer

    Returns:
        list of MonitoringStation objects
    """

    # Create empty list
    at_risk_list = []

    # Loop over all station objects in stations list
    for station in stations:

        # Check if station has all available & consistent data
        if station.relative_water_level() != None:

            # Create tuple of [station object, relative water level]
            at_risk_tuple =

            # Add tuple to list

    # sort list by relative level in descending order
# endregion
