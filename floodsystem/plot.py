import matplotlib.pyplot as plt

# region Task 2E
# water level data against time for a station
# include typical high, low lines
# labelled axes
# station name is plot title


def plot_water_levels(stations, dates, levels):
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
