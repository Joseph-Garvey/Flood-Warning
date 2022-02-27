import matplotlib.pyplot as plt


#region Task 2E
# water level data against time for a station
# include typical high, low lines
# labelled axes
# station name is plot title
def plot_water_levels(stations, dates, levels):
   print()
   for i in range(stations.len):
        plt.subplot(1, stations.len(), i+1)
        plt.plot(dates, levels[i])    
        # Add labels, rotate and add plot title
        plt.title(stations[i].name)
        plt.xlabel('Date')
        plt.ylabel('Water Level (m)')
        plt.xticks(rotation = 45)
    print()

#endregion