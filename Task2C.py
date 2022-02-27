# region imports
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
# endregion

"""prints the names of the 10 stations at which the current relative level is highest, with the relative level beside each station name"""

# region demo


def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    station_objects_risk_list = stations_highest_rel_level(stations, 10)
    for station_object in station_objects_risk_list:
        print(station_object.name, station_object.relative_water_level())


# endregion
if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
