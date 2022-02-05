from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations


def run():
    """Task 1F: prints a list of station names, in alphabetical order, for stations with inconsistent data"""

    # Build list of stations
    stations = build_station_list()

    # Create empty list
    incons_station_names = []

    # Loop over incons_stations list
    for station in inconsistent_typical_range_stations(stations):
        # Get station names
        incons_station_names.append(station.name)

    # Sort list by alphabetical order & print
    sorted_incons_station_names = sorted(incons_station_names)
    print(sorted_incons_station_names)


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
