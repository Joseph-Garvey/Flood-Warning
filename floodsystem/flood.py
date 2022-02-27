

def stations_level_over_threshold(stations, tol):
    """returns a list of tuples, where each tuple holds (i) a station (object) at which the latest relative water level is over tol and (ii) the relative water level at the station. The returned list should be sorted by the relative level in descending order"""
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
