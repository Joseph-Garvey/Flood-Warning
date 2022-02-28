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
    dates = []
    levels = []
    final_station_list = []

    # Create list of top N stations
    # pull first N with highest rel level
    selected_stations_list = stations_highest_rel_level(stations, N)
    # check consistency of historical data ie that it has some
    for station in selected_stations_list:

        # Create lists of dates & of level data for past N days
        date_list, level_list = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))

        if(len(date_list) != 0 or len(level_list) != 0):
            # if consistent, append to new list
            # if not consistent : pull highest rel level (currentlengthofllist +1)

            # check again but start at position of the inconsistent data +1
            final_station_list.append(station)
            dates.append(date_list)
            levels.append(level_list)

        else:
            stations_highest_rel_level(stations, N + 1)[N + 1]

    # Plot
    plot_water_levels(final_station_list, dates, levels)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
