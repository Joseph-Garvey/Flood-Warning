
from floodsystem.station import MonitoringStation
from floodsystem.predictor import predictor, assigning_risk

# Create list of dummy stations, 1 with consistent & available data, 1 with empty level data, 1 with empty typical data, 1 with inconsistent low/high data
station_A = MonitoringStation('ID A', 'Measurement ID A', 'Name A', (10.0, 20.0), None, 'Medium River', 'Town A')
station_A.latest_level = 15.0

station_B = MonitoringStation('ID B', 'Measurement ID B', 'Name B', (0.0, 10.0), (1.0, 2.0), 'Big River', 'Town B')
station_B.latest_level = None

station_C = MonitoringStation('ID C', 'Measurement ID C', 'Name C', (0.0, 20.0), (2.0, 1.0), 'Big River', 'Town C')
station_C.latest_level = 10.0

station_D = MonitoringStation('ID D', 'Measurement ID D', 'Name D', (0.0, 20.0), (1.0, 2.0), 'Big River', 'Town D')
station_D.latest_level = 1.5
station_D.der = 2.0

station_E = MonitoringStation('ID E', 'Measurement ID E', 'Name E', (0.0, 20.0), (1.0, 2.0), 'Big River', 'Town E')
station_E.latest_level = 1.9
station_E.der = 1.0

station_F = MonitoringStation('ID F', 'Measurement ID F', 'Name F', (0.0, 20.0), (1.0, 2.0), 'Big River', 'Town F')
station_F.latest_level = 2.0
station_F.der = 2.0

station_list = [station_A, station_B, station_C, station_D, station_E, station_F]


def test_predictor():
    predictor(station_list, gradient_weight=0.5, rel_weight=0.5)

    # assert that attribute type is a float
    for station in station_list:
        # TODO #10 what about NoneType data? should we edit predictor.py to remove stations with None values for levels etc.
        assert type(station.station_risk) == float
    # assert that attribute value is as expected
    # TODO assert station_A.station_risk == None
    # TODO assert station_B.station_risk == None
    # TODO assert station_C.station_risk == None
    assert station_D.station_risk == 1.25
    assert station_E.station_risk == 0.95
    assert station_F.station_risk == 1.5


def test_assigning_risk():
    assigning_risk(station_list, severe_threshold=, high_threshold=, moderate_threshold=)
    # assert that attribute type is a string
    for station in station_list:
        # TODO what about NoneType data? should we edit predictor.py to remove stations with None values for levels etc.
        assert type(station.risk_label) == str

    # assert that attribute value is as expected
    # TODO assert station_A.risk_label == None
    # TODO assert station_B.risk_label == None
    # TODO assert station_C.risk_label == None
    # TODO assert station_D.risk_label ==
    # TODO assert station_E.risk_label == 0.95
    # TODO assert station_F.risk_label == 1.5
