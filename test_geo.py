from floodsystem.geo import *

def test_distance():
    coord1 = [15.0185, 30.2026]
    coord2 = [23.5076, 1.101]
    assert round(distance(coord1, coord2), 6) == 3190.13