from geopy.distance import geodesic

lng1 = 119.375145
lat1 = 25.347994
lng2 = 121.555512
lat2 = 29.874471

print(geodesic((lat1, lng1), (lat2, lng2)).km)


