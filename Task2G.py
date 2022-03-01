import datetime

from sqlalchemy import true
# input yesterdays grad, todays
import floodsystem.analysis
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    # Build list of stations
    stations = build_station_list()
    # filter stations to those with consistent data
    filtered = filter(lambda s: (s.typical_range_consistent == True), stations)
    stations = list(filtered)
    # Update latest level data for all stations
    update_water_levels(stations)
    # flood.py retrieve all data
    # compute poly, d for each station

    # retrieve scores for each station [Irfan]

    # assigning function [Irfan]

    # sort list

    # TODO Relative to usual


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    print("Predicting Floods.....")
    run()
