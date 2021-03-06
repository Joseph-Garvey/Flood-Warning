"""Unit test for the flood module"""

from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level

# Create list of dummy stations, 1 with consistent & available data, 1 with empty level data, 1 with empty typical data, 1 with inconsistent low/high data
station_A = MonitoringStation('ID A', 'Measurement ID A', 'Name A', (10.0, 20.0), None, 'Medium River', 'Town A')
station_A.latest_level = 15.0

station_B = MonitoringStation('ID B', 'Measurement ID B', 'Name B', (0.0, 10.0), (1.0, 2.0), 'Big River', 'Town B')
station_B.latest_level = None

station_C = MonitoringStation('ID C', 'Measurement ID C', 'Name C', (0.0, 20.0), (2.0, 1.0), 'Big River', 'Town C')
station_C.latest_level = 10.0

station_D = MonitoringStation('ID D', 'Measurement ID D', 'Name D', (0.0, 20.0), (1.0, 2.0), 'Big River', 'Town D')
station_D.latest_level = 1.5

station_E = MonitoringStation('ID E', 'Measurement ID E', 'Name E', (0.0, 20.0), (1.0, 2.0), 'Big River', 'Town E')
station_E.latest_level = 1.9

station_F = MonitoringStation('ID F', 'Measurement ID F', 'Name F', (0.0, 20.0), (1.0, 2.0), 'Big River', 'Town F')
station_F.latest_level = 2.0

station_list = [station_A, station_B, station_C, station_D, station_E, station_F]


def test_stations_level_over_threshold():

    threshold_list = stations_level_over_threshold(station_list, 0.8)
    # assert that type is list
    assert type(threshold_list) == list
    # assert that returned list is of correct length
    assert len(threshold_list) == 2
    # assert that type within list is a tuple
    for threshold_data in threshold_list:
        assert type(threshold_data) == tuple
        # assert that 1st object is a MonitoringStation object
        assert type(threshold_data[0]) == MonitoringStation
        # assert that 2nd object is a float
        assert type(threshold_data[1]) == float


def test_stations_highest_rel_level():

    rel_level_list = stations_highest_rel_level(station_list, 3)

    # assert that output type is a list
    assert type(rel_level_list) == list

    # assert that list items are MonitoringStation objects
    for i in range(len(rel_level_list)):
        assert type(rel_level_list[i]) == MonitoringStation

    # assert that order is descending in order
    assert rel_level_list[0].relative_water_level > rel_level_list[1].relative_water_level > rel_level_list[2].relative_water_level

    # assert that length of list is N
    assert len(rel_level_list) == 3
