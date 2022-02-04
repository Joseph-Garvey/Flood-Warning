from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance


def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()

    # List of stations & distance:
    stations_distance_list = stations_by_distance(stations, (52.2053, 0.1218))

    # TO DO: Sort list

    # Filter top & bottom 10
    closest = stations_distance_list[:10]
    furthest = stations_distance_list[-10:]

    # Create list of tuples containing name, town, distance
    closest_list = []
    furthest_list = []

    for tuple in closest:
        entry = tuple[0].name, tuple[0].town, tuple[1]
        closest_list.append(entry)

    for tuple in furthest:
        entry = tuple[0].name, tuple[0].town, tuple[1]
        furthest_list.append(entry)

    print("Closest 10:", closest_list)
    print("Furthest 10:", furthest_list)


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
