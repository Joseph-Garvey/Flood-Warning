import numpy as np
import matplotlib.dates as dt
import matplotlib.pyplot as plt

# implement function
    # input: water level time history (dates, levels) for a station
    # computes least-squares fit polynomial of a degree p to water level data
    # returns:
        # tuple of 
            # polynomaial object
            # shift of time (date) axis
#task 2F
#TODO #2 return correct object
def polyfit(dates, levels, p):
    dates = dt.date2num(dates)
    p_coeff = np.polyfit(dates - dates[0], levels, p)
    poly = np.poly1d(p_coeff)
    return poly, dt.date2num(dates[0])

