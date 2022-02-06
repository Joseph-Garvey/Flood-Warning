# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town


# region Task 1F Testing

# Testing Task 1F part i - irfan
def test_typical_range_consistent():
    # Create 3 dummy stations, 1 with consistent data, 1 with empty data, 1 with inconsistent low/high data
    station_A = MonitoringStation('ID A', 'Measurement ID A', 'Name A', (10.0, 40.0), None, 'Medium River', 'Town A')
    station_B = MonitoringStation('ID B', 'Measurement ID B', 'Name B', (0.0, 10.0), (1.0, 2.0), 'Big River', 'Town B')
    station_C = MonitoringStation('ID C', 'Measurement ID C', 'Name C', (0.0, 20.0), (2.0, 1.0), 'Big River', 'Town C')

    # Assert A & C are False, B is True
    assert station_A.typical_range_consistent() == False
    assert station_B.typical_range_consistent() == True
    assert station_C.typical_range_consistent() == False

# Testing Task 1F part ii - irfan


def test_inconsistent_typical_range_stations():
    # Create list of 3 dummy stations, 1 with consistent data, 1 with empty data, 1 with inconsistent low/high data
    station_A = MonitoringStation('ID A', 'Measurement ID A', 'Name A', (10.0, 40.0), None, 'Medium River', 'Town A')
    station_B = MonitoringStation('ID B', 'Measurement ID B', 'Name B', (0.0, 10.0), (1.0, 2.0), 'Big River', 'Town B')
    station_C = MonitoringStation('ID C', 'Measurement ID C', 'Name C', (0.0, 20.0), (2.0, 1.0), 'Big River', 'Town C')

    station_list = [station_A, station_B, station_C]

    # Assert that output is a list
    assert type(inconsistent_typical_range_stations(station_list)) == list

    # Assert that each entry has the correct type
    assert type(inconsistent_typical_range_stations(station_list)[0]) == MonitoringStation

    # Assert that list has length 2
    assert len(inconsistent_typical_range_stations(station_list)) == 2

    # Assert that all are False
    assert inconsistent_typical_range_stations(station_list)[0].typical_range_consistent() == False
    assert inconsistent_typical_range_stations(station_list)[1].typical_range_consistent() == False

# endregion
