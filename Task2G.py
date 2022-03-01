import datetime
from operator import attrgetter
from floodsystem.analysis import gradientcalc, polyfit
from floodsystem.flood import stations_highest_rel_level_consistent, stations_historical
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.predictor import predictor, assigning_risk
import matplotlib.dates as dt

def run():
    # Build list of stations
    stations = build_station_list()
    # filter stations to those with consistent data
    filtered = filter(lambda s: (s.typical_range_consistent == True), stations)
    stations = list(filtered)
    # Update latest level data for all stations
    update_water_levels(stations)
    # flood.py retrieve all data [Irfan]
    stations, dates, levels = stations_highest_rel_level_consistent(stations, 40, 0.5)
    # compute poly, d for each station
    for i in range(len(stations)):
        poly = polyfit(dates[i], levels[i], 4)
        #yesterdays date
        stations[i].der = gradientcalc(poly, -0.5)
    # retrieve scores for each station [Irfan]
    gradient_weight = 0.5 
    rel_weight = 0.5
    stations = predictor(stations, gradient_weight, rel_weight)
    # assigning function [Irfan]
    severe_threshold = 10.0
    high_threshold = 7.5
    moderate_threshold = 5.0
    stations = assigning_risk(stations, severe_threshold, high_threshold, moderate_threshold)
    # Sort by descending risk
    stations.sort(key=attrgetter('station_risk'), reverse=True)
    for station in stations:
        print(station.name, str(station.station_risk))

    # TODO Relative to usual


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    print("Predicting Floods.....")
    run()
