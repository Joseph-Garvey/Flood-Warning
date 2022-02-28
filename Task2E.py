from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import datetime


def run():
    # Build list of stations
    stations = build_station_list()
    # Update latest level data for all stations
    update_water_levels(stations)

    # Plot water levels over past 10 days for 5 stations at which current rel. water level is highest.

    N = 5  # Number of stations
    dt = 10  # Number of days

    # Create list of top N stations
    selected_stations_list = stations_highest_rel_level(stations, N)

    # Find station
    for station in selected_stations_list:
        selected_station = station

    # Create list of level data for past 10 days
    date_list, level_list = fetch_measure_levels(selected_station.measure_id, dt=datetime.timedelta(days=dt))

    # Plot
    plot_water_levels(selected_stations_list, date_list, level_list)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
