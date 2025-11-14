import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

figure_window = plt.figure(figsize=(10, 8))
usa_map = Basemap(projection='stere', lat_0=90, lon_0=-105, llcrnrlat=23.41, 
                  urcrnrlat=45.44, llcrnrlon=-118.67, urcrnrlon=-64.52, 
                  rsphere=6371200., resolution='l', area_thresh=10000)

usa_map.drawmapboundary()
usa_map.drawstates()
usa_map.drawcoastlines()
usa_map.drawcountries()
latitude_lines = np.arange(0., 90, 10.)
usa_map.drawparallels(latitude_lines, labels=[1, 0, 0, 0], fontsize=10)
longitude_lines = np.arange(-110., -60., 10.)
usa_map.drawmeridians(longitude_lines, labels=[0, 0, 0, 1], fontsize=10)

city_data = pd.read_csv(r"2014_us_cities.csv")

latitude_values = np.array(city_data["lat"])
longitude_values = np.array(city_data["lon"])
population_values = np.array(city_data["pop"], dtype=float)

for index in range(len(latitude_values)):
    bubble_size = (population_values[index] / np.max(population_values)) * 1000 
    map_x, map_y = usa_map(longitude_values[index], latitude_values[index])
    if population_values[index] >= 2000000:
        bubble_color = 'purple'
    elif population_values[index] >= 500000:
        bubble_color = 'green'
    else:
        bubble_color = 'orange'
    usa_map.scatter(map_x, map_y, s=bubble_size, c=bubble_color)

plt.title('2014年美国部分城镇的人口分布情况')
plt.show()
