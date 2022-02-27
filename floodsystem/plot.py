import matplotlib.pyplot as plt


#region Task 2E
# water level data against time for a station
# include typical high, low lines
# labelled axes
# station name is plot title
def plot_water_levels(station, dates, levels):
    # Plot Data
    plt.plot(dates, levels)
    # Add labels, rotate and add plot title
    plt.xlabel('Date')
    plt.ylabel('Water Level (m)')
    plt.xticks(rotation = 45)
    plt.title(station.name)
    # Display Layout and Plot
    plt.tight_layout()
    plt.show()

#endregion