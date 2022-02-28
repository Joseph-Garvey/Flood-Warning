import matplotlib.pyplot as plt

# region Task 2E
# water level data against time for a station
# include typical high, low lines
# labelled axes
# station name is plot title


def plot_water_levels(stations, dates, levels):
    # reminder TODO #3 check no more than 6 plotted
    for i in range(len(stations)):
        plt.subplot(1, len(stations), i + 1)
        plt.plot(dates, levels[i])
        plt.plot(dates, stations[i].typical_range[0])
        plt.plot(dates, stations[i].typical_range[1])

        # Add labels, rotate and add plot title
        plt.title(stations[i].name)
        plt.xlabel('Date')
        plt.ylabel('Water Level (m)')
        plt.xticks(rotation=45)
    plt.show()

# endregion
