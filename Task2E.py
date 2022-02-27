from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    # Build list of stations
    stations = build_station_list()
    # Update latest level data for all stations
    update_water_levels(stations)

    

    #REMINDER TODO
    # Plot water levels over past 10 days for 5 stations at which current rel. water level is highest.


