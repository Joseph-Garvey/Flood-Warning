# dependencies
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

# main
def run():
    """Requirements for Task 1C"""

    # Build list of stations
    stations = build_station_list()
    # Filter list by stations within 10km of Cambridge City Centre
    # City Centre has coords (52.2053, 0.1218)
    stations_filtered = stations_within_radius(stations, (52.2053, 0.1218), 10)
    # sort alphabetical
    stations_filtered.sort()
    # output the filtered list.
    for station in stations_filtered:
        print(station.name)

if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()