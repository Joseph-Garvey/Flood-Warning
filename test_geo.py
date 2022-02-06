from floodsystem.station import MonitoringStation
from floodsystem.geo import *

#region Test Variables
# Create 7 dummy stations
# Requires:
# Different distances
# 1 river with three stations
# 1 river with two stations
# 2 rivers with one station
# Some distances outside radius x and some inside radius x
# At least 1 with no typical range data
# At least 2 with inconsistent typical range data
station_1 = MonitoringStation('ID 1', 'Measurement ID 1', 'Name 1', (10.0, 10.0), (1.0, 2.0), 'Small River 1', 'Town 1')
station_2 = MonitoringStation('ID 2', 'Measurement ID 2', 'Name 2', (10.0, 20.0), (1.0, 2.0), 'Small River 2', 'Town 2')
station_3 = MonitoringStation('ID 3', 'Measurement ID 3', 'Name 3', (10.0, 30.0), (1.0, 2.0), 'Medium River', 'Town 3')
station_4 = MonitoringStation('ID 4', 'Measurement ID 4', 'Name 4', (10.0, 40.0), (), 'Medium River', 'Town 4')
station_5 = MonitoringStation('ID 5', 'Measurement ID 5', 'Name 5', (0.0, 10.0), (1.0, 2.0), 'Big River', 'Town 5')
station_6 = MonitoringStation('ID 6', 'Measurement ID 6', 'Name 6', (0.0, 20.0), (2.0, 1.0), 'Big River', 'Town 6')
station_7 = MonitoringStation('ID 7', 'Measurement ID 7', 'Name 7', (0.0, 30.0), (2.0, 1.0), 'Big River', 'Town 7')

test_stations = [station_1, station_2, station_3, station_4, station_5, station_6, station_7]
#endregion

#region Tests
def test_distance():
    coord1 = [15.0185, 30.2026]
    coord2 = [23.5076, 1.101]
    assert round(distance(coord1, coord2), 2) == 3190.13

# Task 1B Tests - irfan
def test_stations_by_distance():

    # Requirement: returns a list of (station, distance) tuples
    test_distance_list = stations_by_distance(test_stations, (10.0, 10.0))

    # assert that it is a list
    assert type(test_distance_list) == list

    # assert that all 7 stations are returned
    assert len(test_distance_list) == 7

    # assert that tuple contents are of the correct type
    assert type(test_distance_list[0]) == tuple
    assert type(test_distance_list[0][0]) == MonitoringStation
    assert type(test_distance_list[0][1]) == float

    # assert that list is sorted by distance
    for i in range(len(test_distance_list) - 1):
        assert test_distance_list[i][1] <= test_distance_list[i + 1][1]

# Task 1C Tests - joe
def test_stations_within_radius():
    """Tests the functions used within Task 1C.
    Test List will return a list of stations within the test area.
    Expected Values: [Station 1, Station 2, Station 5, Station 6]
    """
    # obtain test list from function being tested
    # expected result known and checked
    test_list = stations_within_radius(test_stations, (0.0,0.0), (2500.0))
    assert len(test_list) == 4
    assert type(test_list) == list
    assert station_1 in test_list
    assert station_2 in test_list
    assert station_3 not in test_list
    assert station_4 not in test_list
    assert station_5 in test_list
    assert station_6 in test_list
    assert station_7 not in test_list

# Task 1D Tests - joe
def test_rivers_with_station():
    """Tests the function used by Task 1D i
    Test List should return a (container) of rivers without duplicates.
    """
    #   nb it is not explicitly stated what container type should be used,
    #   however as this program uses sets, this is still tested for.

    # in the test data there are 4 rivers
    test_set = rivers_with_station(test_stations)
    assert len(test_set) == 4
    assert type(test_set) == set ## there will be zero duplicate values by virtue of the type being a set,
    # therefore, it is not necessary to test for duplicate values.

def test_stations_by_river():
    """Tests the function used by Task 1D ii"""
    # gather test data from function
    test_dict = stations_by_river(test_stations)
    # assert return correct type
    assert type(test_dict) == dict
    # testing for duplicates unnecessary as dict only allows unique keys.
    # assert correct number of rivers.
    assert len(test_dict) == 4
    # asset each river exists as a key
    assert "Big River" in test_dict
    assert "Medium River" in test_dict
    assert "Small River 1" in test_dict
    assert "Small River 2" in test_dict
    # assert each river has the correct number of stations
    # assert big rivers have 3 stations, medium 2, small 1.
    assert len(test_dict["Big River"]) == 3
    assert len(test_dict["Medium River"]) == 2
    assert len(test_dict["Small River 1"]) == len(["Small River 2"]) == 1
    # assert correct stations at each river
    assert station_1 in test_dict["Small River 1"]
    assert station_2 in test_dict["Small River 2"]
    assert station_3 in test_dict["Medium River"]
    assert station_4 in test_dict["Medium River"]
    assert station_5 in test_dict["Big River"]
    assert station_6 in test_dict["Big River"]
    assert station_7 in test_dict["Big River"]
    
# Task 1E Tests - joe
def test_rivers_by_station_number():
    test_list = rivers_by_station_number(test_stations, 3)
    # should produce 5 stations
    assert test_list[0][0] == "Big River"  # river with most stations at top of list
    assert len(test_list) == 4  # assert that same no as nth entry also returned
    assert type(test_list) == list  # assert that it is a list
    # assert list is ordered
    for i in range(len(test_list) - 1):
        assert test_list[i][1] >= test_list[i + 1][1]
#endregion