
from floodsystem.station import MonitoringStation
from floodsystem.predictor import predictor, assigning_risk

# Create list of dummy stations, 1 with consistent & available data, 1 with empty level data, 1 with empty typical data, 1 with inconsistent low/high data

station_D = MonitoringStation('ID D', 'Measurement ID D', 'Name D', (0.0, 20.0), (1.0, 2.0), 'Big River', 'Town D')
station_D.latest_level = 1.5
station_D.der = 2.0

station_E = MonitoringStation('ID E', 'Measurement ID E', 'Name E', (0.0, 20.0), (1.0, 2.0), 'Big River', 'Town E')
station_E.latest_level = 1.9
station_E.der = 1.0

station_F = MonitoringStation('ID F', 'Measurement ID F', 'Name F', (0.0, 20.0), (1.0, 2.0), 'Big River', 'Town F')
station_F.latest_level = 2.0
station_F.der = 2.0

station_list = [station_D, station_E, station_F]


def test_predictor():
    predictor(station_list, gradient_weight=1, rel_weight=5, abs_weight=15)

    # assert that attribute type is a float
    for station in station_list:
        assert type(station.station_risk) == float
    # assert that attribute value is as expected
    assert station_D.station_risk == 0.75
    assert station_E.station_risk == 1.9166666666666663
    assert station_F.station_risk == 2.4166666666666665


def test_assigning_risk():
    assigning_risk(station_list, severe_threshold=3, high_threshold=2.25, moderate_threshold=1.5)
    # assert that attribute type is a string
    for station in station_list:
        assert type(station.risk_label) == str

    # assert that attribute value is as expected

    assert station_D.risk_label == 'low'
    assert station_E.risk_label == 'moderate'
    assert station_F.risk_label == 'high'
