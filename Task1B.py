from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance


def run():
    """Task 1B: prints a list of tuples (station name, town, distance) for the 10 closest and the 10 furthest stations from the Cambridge city centre, (52.2053, 0.1218)"""

    # Build list of stations
    stations = build_station_list()

    # List of stations & distance
    stations_distance_list = stations_by_distance(stations, (52.2053, 0.1218))

    # Filter top & bottom 10
    closest = stations_distance_list[:10]
    furthest = stations_distance_list[-10:]

    # Create empty lists
    closest_list = []
    furthest_list = []

    # Update lists with tuples containing name, town, distance
    for tuple in closest:
        entry = tuple[0].name, tuple[0].town, tuple[1]
        closest_list.append(entry)

    for tuple in furthest:
        entry = tuple[0].name, tuple[0].town, tuple[1]
        furthest_list.append(entry)

    # Print closest & furthest lists
    print("Closest 10:", closest_list)
    print("Furthest 10:", furthest_list)


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
