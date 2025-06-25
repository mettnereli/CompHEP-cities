import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

cities = [["Chicago", 41.8781, 87.6298],
          ["Boston", 42.3555, 71.0565],
          ["Madison", 43.0722, 89.4008],
          ["San Diego", 32.7157, 117.1611]]
scale = 5

map = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
        projection='lcc',lat_1=32,lat_2=45,lon_0=-95)

map.drawstates()

# Get the location of each city and plot it
for (city, latitude, longitude) in cities:
    x, y = map(longitude, latitude)
    map.plot(x, y, marker='o',color='Red')
plt.show()

