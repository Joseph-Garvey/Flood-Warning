import datetime
from operator import attrgetter
import time
from floodsystem.analysis import gradientcalc, polyfit
from floodsystem.flood import stations_highest_rel_level_consistent, stations_historical
from floodsystem.plot import plot_water_level_with_fit, plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.predictor import predictor, assigning_risk
import matplotlib.dates as dt


def run():
    tic = time.perf_counter()
    # Build list of stations
    stations = build_station_list()
    # filter stations to those with consistent data
    filtered = filter(lambda s: (s.typical_range_consistent == True), stations)
    stations = list(filtered)
    # Update latest level data for all stations
    update_water_levels(stations)
    # flood.py retrieve all data [Irfan]
    simduration = 2
    stations, dates, levels = stations_highest_rel_level_consistent(
        stations, 200, simduration)  # top 200 rel_level stations
    # stations, dates, levels = stations_highest_rel_level_consistent(stations, len(stations), simduration) #stations historical for all
    #stations, dates, levels = stations_historical(stations, simduration)

    # compute poly, d for each station
    for i in range(len(stations)):
        poly = polyfit(dates[i], levels[i], 4)
        # yesterdays date
        stations[i].der = gradientcalc(poly[0], -simduration / 2)
    # retrieve scores for each station [Irfan]
    gradient_weight = 1
    rel_weight = 5
    abs_weight = 15
    stations = predictor(stations, gradient_weight, rel_weight, abs_weight)
    # assigning function [Irfan]
    severe_threshold = 3
    high_threshold = 2.25
    moderate_threshold = 1.5
    stations = assigning_risk(stations, severe_threshold, high_threshold, moderate_threshold)
    # Sort by descending risk
    stations.sort(key=attrgetter('station_risk'), reverse=True)
    for station in stations:
        if((station.risk_label == "severe") or (station.risk_label == "high")):
            print(station.name, station.risk_label)
    # should have done moderate if above typical high
    toc = time.perf_counter()
    print(f"Warned floods in {toc - tic:0.4f} seconds")


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    print("*****************Predicting Floods.....***********")
    run()
