from math import radians, sin, cos, sqrt, atan2
from Location import Location

def haversine(location1 : Location, location2 : Location):
    # GET LATITUDE AND LONGTITUDE
    lat1 = location1.getLat()
    long1 = location1.getLong()
    lat2 = location2.getLat()
    long2 = location2.getLong()

    # EARTH RADIUS (km)
    R = 6371

    # CONVERT LATITUDE AND LONGTITUDE TO RADIANS
    lat1, long1, lat2, long2 = map(radians, [lat1, long1, lat2, long2])

    # FIND DELTA OF LATITUDE AND LONGTITUDE
    dlat = lat2 - lat1
    dlon = long2 - long1

    # HAVERSINE FORMULA
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    
    return distance