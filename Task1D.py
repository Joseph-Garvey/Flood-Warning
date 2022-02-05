#region dependencies
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river
#endregion

#region main
def run():
    """Requirements for Task 1D"""
    # Build list of stations
    stations = build_station_list()
    # print how many rivers have at least one monitoring station
    print(len(rivers_with_station))
    # print first 10 in alphabetical order
    print(stations_by_river)

if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()

#endregion