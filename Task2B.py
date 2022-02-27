from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

"""prints the name of each station at which the current relative level is over 0.8, with the relative level alongside the name (do not forget to handle the cases of inconsistent range data)"""


def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Create empty list
    #list = []

    # print(stations[0].relative_water_level())

    # Create list of tuples of station objects & relative water levels above 0.8
    station_level_list = stations_level_over_threshold(stations, 0.8)

    # Create tuple of names & relative water levels to tuple
    print(station_level_list)


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
