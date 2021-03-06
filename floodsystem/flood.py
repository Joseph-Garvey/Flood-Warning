# region imports
from .station import MonitoringStation
from operator import attrgetter
from .datafetcher import fetch_measure_levels
import datetime
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
        if (station.relative_water_level != None) and (station.relative_water_level > tol):
            # Create tuple
            over_threshold_tuple = (station, station.relative_water_level)

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
        if station.relative_water_level != None:

            # Add station object to list
            at_risk_list.append(station)

    # Sort list by relative level in descending order
    at_risk_list.sort(key=attrgetter('relative_water_level'), reverse=True)

    # Slice list to first N objects
    first_N_at_risk = at_risk_list[:N]

    return first_N_at_risk

    # sort list by relative level in descending order
# endregion


def stations_highest_rel_level_consistent(source_stations, N, dt):
    """Returns rivers with highest relative level, but only those with historical data.
    Also returns historical data.

    RETURNS: List of Stations, List of Dates, List of Levels
    """
    stations_to_be_plotted = []  # empty list of stations
    dates = []  # empty list of date lists
    levels = []  # empty list of level lists

    # pull first N with highest rel level
    stations = stations_highest_rel_level(source_stations, N)

    i = 0
    while(len(stations_to_be_plotted) < N):
        # if we have searched as many items as we initially retrieved, retrieve one more than the current number pulled.
        if(i >= N - 1):
            stations = stations_highest_rel_level(source_stations, i + 2)
            # this could just as easily be len(stations) + 1 instead of i
        # retrieve list
        date_list, level_list = fetch_measure_levels(stations[i].measure_id, dt=datetime.timedelta(days=dt))
        # check validity
        if(len(date_list) == 0 or len(level_list) == 0):
            i += 1
            continue  # skip if invalid
        # add to list if valid
        stations_to_be_plotted.append(stations[i])
        dates.append(date_list)
        levels.append(level_list)
        i += 1

    return stations_to_be_plotted, dates, levels


def stations_historical(stations, dt):
    """RETURNS: List of Stations, List of Dates, List of Levels"""

    stations_new = []  # empty new list of stations
    dates = []  # empty list of date lists
    levels = []  # empty list of level lists

    # retrieve list
    for i in range(len(stations)):
        date_list, level_list = fetch_measure_levels(stations[i].measure_id, dt=datetime.timedelta(days=dt))
        # check validity
        if(len(date_list) == 0 or len(level_list) == 0):
            continue  # skip if invalid
        # add to list if valid
        stations_new.append(stations[i])
        dates.append(date_list)
        levels.append(level_list)
        print("Fetched station " + str(i) + " out of " + str(len(stations)) + " stations.")

    return stations_new, dates, levels
