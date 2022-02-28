import numpy as np
import matplotlib.dates as time
# implement function
    # input: water level time history (dates, levels) for a station
    # computes least-squares fit polynomial of a degree p to water level data
    # returns:
        # tuple of 
            # polynomial object
            # shift of time (date) axis
#task 2F
def polyfit(dates, levels, p):
    dates = time.date2num(dates)
    p_coeff = np.polyfit(dates, levels, p)
    poly = np.poly1d(p_coeff)
    