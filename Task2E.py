from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
import datetime


def run():
    # Build list of stations
    stations = build_station_list()
    # Update latest level data for all stations
    update_water_levels(stations)

    # Plot water levels over past 10 days for 5 stations at which current rel. water level is highest.

    # Create list of past 5 days
    date_list = []

    for i in range(5):
        date_item = datetime.date.today() - datetime.timedelta(days=i)
        date_list.append(date_item)

    # Create list of top N stations
    selected_stations_list = stations_highest_rel_level(stations, 5)

    # Create list of latest_level data for past 5 days

    # Plot
    plot_water_levels(selected_stations_list, date_list, levels)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
