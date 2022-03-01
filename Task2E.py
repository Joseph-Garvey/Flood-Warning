from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level_consistent


def run():
    # Build list of stations
    source_stations = build_station_list()
    # Update latest level data for all stations
    update_water_levels(source_stations)

    # Plot water levels over past 10 days for 5 stations at which current rel. water level is highest.

    N = 5  # Number of stations
    dt = 10  # Number of days

    stations_to_be_plotted, dates, levels = stations_highest_rel_level_consistent(source_stations, N, dt)

    plot_water_levels(stations_to_be_plotted, dates, levels)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
