import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

cities = [["Chicago", 41.8781, -87.6298],
          ["Boston", 42.3555, -71.0565],
          ["Madison", 43.0722, -89.4008],
          ["San Diego", 32.7157, -117.1611],
          ["Los Angeles", 34.0522, -118.2437],
          ["San Francisco", 37.7749, -122.4194],
          ["Seattle", 47.6062, -122.3321],
          ["New York", 40.7128, -74.0060],
          ["Washington DC", 38.9072, -77.0369],
          ["Miami", 25.7617, -80.1918],
          ["Houston", 29.7604, -95.3698],
          ["Dallas", 32.7767, -96.7970],
          ["Phoenix", 33.4484, -112.0740],
          ["Denver", 39.7392, -104.9903],
          ["Atlanta", 33.7490, -84.3880],
          ["Orlando", 28.5383, -81.3792],
          ["Las Vegas", 36.1699, -115.1398],
          ["Portland", 45.5051, -122.6750],
          ["Salt Lake City", 40.7608, -111.8910],  
          ]
scale = 5

#Map the USA with rivers
plt.figure(figsize=(12, 8))
plt.title('Cities in the USA with Rivers', fontsize=16)
plt.xlabel('Longitude', fontsize=12)
plt.ylabel('Latitude', fontsize=12) 
map = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
        projection='lcc',lat_1=32,lat_2=45,lon_0=-95)

# Draw states
map.drawstates()

# Draw coastlines
map.drawcoastlines()

# Draw mexican and canadian borders
map.drawcountries()


# Headings for the cities
for (city, latitude, longitude) in cities:
    x, y = map(longitude, latitude)
    plt.text(x, y, city, fontsize=9, ha='right', va='bottom', color='red')

# Get the location of each city and plot it
for (city, latitude, longitude) in cities:
    x, y = map(longitude, latitude)
    map.plot(x, y, marker='o', color='Red')

#add NASA bluemarble image
map.bluemarble()
# Draw rivers
map.drawrivers()

plt.show()
plt.savefig('cities_map_wRivers.png')