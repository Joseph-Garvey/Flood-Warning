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
    dates = []  # empty list of date lists
    levels = []  # empty list of level lists
    final_station_list = []  # empty list of stations

    # pull first N with highest rel level
    selected_stations = stations_highest_rel_level(stations, N)
    # check consistency of historical data ie that it has some

    counter = 0

    for station in selected_stations:
        # while counter < N:
        date_list, level_list = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        if(len(date_list) == 0 or len(level_list) == 0):
            continue
        # Append current station to final list, and append corresponding data to data lists
        final_station_list.append(station)
        dates.append(date_list)
        levels.append(level_list)

        counter += 1

        if counter < N:
            stations_highest_rel_level(stations, N + 1)[N + 1]
            # TODO what the hell

        counter += 1
        # Create lists of dates & of level data for past N days

        # if consistent, append to new list
        # if not consistent : pull highest rel level (currentlengthofllist +1)

        # check again but start at position of the inconsistent data +1

        else:

            # Plot
    plot_water_levels(final_station_list, dates, levels)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
