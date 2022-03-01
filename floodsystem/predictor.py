from .station import MonitoringStation
from .analysis import polyfit, gradientcalc


def predictor(stations, gradient_weight, rel_weight):
    """assigns an attribute 'station_risk' to each MonitoringStation object based on a weighted sum of rel_water_level & gradient

    Parameters:
        stations = list of MonitoringStation objects \n
        gradient_weight = weight of gradient \n
        relative_weight = weight of rel_water_level
    """
    for station in stations:
        station_risk = (gradient_weight * (station.der) + rel_weight *
                        (station.relative_water_level)) / (gradient_weight + rel_weight)
        station.station_risk = station_risk

    return stations


def assigning_risk(stations, severe_threshold, high_threshold, moderate_threshold):
    """assigns an attribute string (1 of 4: ‘severe’, ‘high’, ‘moderate’ or ‘low’) to each station object

    Parameters:
        stations = list of MonitoringStation objects \n
        thresholds = floats that determine what station_risk values count as each label
    """

    for station in stations:
        if station.station_risk > severe_threshold:
            risk_label = "severe"
        elif station.station_risk > high_threshold:
            risk_label = "high"
        elif station.station_risk > moderate_threshold:
            risk_label = "moderate"
        else:
            risk_label = "low"

        station.risk_label = risk_label

    return stations