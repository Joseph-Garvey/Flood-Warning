from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level
from floodsystem.analysis import polyfit
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list

def run():
    # Build list of stations
    stations = build_station_list()
    # Update latest level data for all stations
    update_water_levels(stations)
    #TODO #1 can copy off of 2E when it is done
    # 5 stations current rel water level is greatest
    # plot level data last 2 days
    # plot best fit poly of degree 4 against time
    # show typical range low/high on plot
    N = 5  # Number of stations
    dt = 2  # Number of days
    # Create list of top N stations
    selected_stations_list = stations_highest_rel_level(stations, N)
    dates = []
    levels = []
    # assume irfan is done
    #temptest
    station_name = "Bourton Dickler"

    # Find station
    station_cam = None
    for station in stations:
        if station.name == station_name:
            station_cam = station
            break
    dt = 10
    dates, levels = fetch_measure_levels(station_cam.measure_id, dt=datetime.timedelta(days=dt))

    poly, d0 = polyfit(dates, levels, 5)
    plot_water_level_with_fit(station_cam, dates, levels, poly)

    print("foo")

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
