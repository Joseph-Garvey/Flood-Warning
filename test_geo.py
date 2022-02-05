from floodsystem.geo import *
# Test Data consists of:
    # 1 river with three stations - Big River
    # 1 river with two stations - Medium River
    # 2 river with one station

def test_distance():
    coord1 = [15.0185, 30.2026]
    coord2 = [23.5076, 1.101]
    assert round(distance(coord1, coord2), 6) == 3190.13

#testing task 1e
def test_rivers_by_station_number():
    list = rivers_by_station_number(test_stations, 3)
    # should produce 5 stations
    assert list[0][0].name == "Big River" # river with most stations at top of list
    assert len(list) == 4 # assert that same no as nth entry also returned
    assert type(list) == list # assert that it is a list
    # assert list is ordered
    for i in range(len(list)-1):
        assert len(list[i][1]) >= len(list[i+1][1])