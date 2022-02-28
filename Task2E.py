from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import datetime


def run():
    # Build list of stations
    source_stations = build_station_list()
    # Update latest level data for all stations
    update_water_levels(source_stations)

    # Plot water levels over past 10 days for 5 stations at which current rel. water level is highest.

    N = 5  # Number of stations
    dt = 10  # Number of days
    dates = []  # empty list of date lists
    levels = []  # empty list of level lists
    stations_to_be_plotted = []  # empty list of stations

    # pull first N with highest rel level
    stations = stations_highest_rel_level(source_stations, N)
    
    i = 0
    while(len(stations_to_be_plotted) < N):
        # if we have searched as many items as we initially retrieved, retrieve one more than the current number pulled.
        if(i >= N-1):
            stations = stations_highest_rel_level(source_stations, i+2) 
            # this could just as easily be len(stations) + 1 instead of i
        #retrieve list
        date_list, level_list = fetch_measure_levels(stations[i].measure_id, dt=datetime.timedelta(days=dt)) 
        # check validity  
        if(len(date_list) == 0 or len(level_list) == 0):
            i += 1
            continue # skip if invalid
        # add to list if valid
        stations_to_be_plotted.append(stations[i])
        dates.append(date_list)
        levels.append(level_list)
        i += 1

    plot_water_levels(stations_to_be_plotted, dates, levels)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
