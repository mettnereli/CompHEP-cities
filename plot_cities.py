import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

cities = [["Chicago",48, -100],
          ["Boston", 49, -90]]
scale = 5

map = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
        projection='lcc',lat_1=32,lat_2=45,lon_0=-95)
#Adding color to the map
map.drawlsmask(land_color='green',ocean_color='lightblue',lakes=True)
map.drawstates(color='black')


# Get the location of each city and plot it
for (city, latitude, longitude) in cities:
    x, y = map(longitude, latitude)
    map.plot(x, y, marker='o',color='Red')
plt.show()

plt.savefig('map.png', dpi=300, bbox_inches='tight')

