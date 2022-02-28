import matplotlib.pyplot as plt
import matplotlib.dates as dt
import numpy as np

# region Task 2E
# water level data against time for a station
# include typical high, low lines
# labelled axes
# station name is plot title
def plot_water_levels(stations, dates, levels):
    # reminder TODO #3 check no more than 6 plotted
    #TODO #4 potential issue where dates of stations are not the same, i should not assume this.
    for i in range(len(stations)):
        plt.subplot(1, len(stations), i + 1)
        plt.plot(dates[i], levels[i])
        plt.axhline(stations[i].typical_range[0])
        plt.axhline(stations[i].typical_range[1])
        # Add labels, rotate and add plot title
        if(len(dates[i]) == 0 or len(levels[i]) == 0):
            plt.title(stations[i].name + "[Data Unavailable]")
        else:
            plt.title(stations[i].name)
        plt.xlabel('Date')
        plt.ylabel('Water Level (m)')
        plt.xticks(rotation=45)
    plt.show()
# endregion

#region Task 2F
# plot water level data and the best fit polynomial
def plot_water_level_with_fit(stations, dates, levels, funcs):
    for i in range(len(stations)):
        plt.subplot(1, len(stations), i + 1)
        plt.plot(dates[i], levels[i])
        plt.axhline(stations[i].typical_range[0])
        plt.axhline(stations[i].typical_range[1])
        plt.xlabel('Date')
        plt.ylabel('Water Level (m)')
        plt.xticks(rotation=45)
        math_date = dt.date2num(dates[i])
        plt.plot(dates[i], funcs[i](math_date - math_date[0]))
        plt.title(stations[0].name)
    plt.suptitle("Measured Level v Best-Fit for Rivers with Highest Relative Level.")

    #dates_interpolated = np.linspace(dates[0], dates[-1], len(dates)*10)
    #math_date = dt.date2num(dates)
    #plt.plot(dates, p(math_date - math_date[0]))
    plt.show()
