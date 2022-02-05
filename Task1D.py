#region dependencies
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
#endregion

#region main
def run():
    """Requirements for Task 1D"""
    # Build list of stations
    stations = build_station_list()
    print(rivers_with_station(stations))


if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()

#endregion