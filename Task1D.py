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
    rivers = rivers_with_station(stations)
    print(len(rivers), "Stations.")
    # print first 10 in alphabetical order
    # sets cannot slice therefore cast to list
    output = list(rivers)
    output.sort()
    print("First 10 -", output[:10])
    # first ten printed in alphabetical order
    # gather river dictionary
    dict_river = stations_by_river(stations)
    # stations on this river
    print(output_station_names(dict_river['River Aire'])) # print station names on river aire
    print(output_station_names(dict_river['River Cam']))
    print(output_station_names(dict_river['River Thames']))
    
def output_station_names(list_stations):
    list_stations.sort()
    output = []
    for station in  list_stations:
        output.append(station.name)
    return output


if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()

#endregion