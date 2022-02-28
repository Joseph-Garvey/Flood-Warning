from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels


def run():
    # Build list of stations
    stations = build_station_list()
    # Update latest level data for all stations
    update_water_levels(stations)

    # Plot water levels over past 10 days for 5 stations at which current rel. water level is highest.

    N = 5

    # Create list of top N stations
    selected_stations_list = stations_highest_rel_level(stations, N)

    # Create list of level data for past 5 days
    level_list = []
    for i in range(N):
        fetch_measure_levels(measure_id, 10)

    # Plot
    plot_water_levels(selected_stations_list, date_list, level_list)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
