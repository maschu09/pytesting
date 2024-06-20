

def normalize_lons(lon:list[float])->list[float]:
    """make sure lons are from -180 to +180 degrees"""
    res = [x-360. if x > 180. else x for x in lon]
    return res

def normalize_lats(lat:list[float])->list[float]:
    """make sure lats are ordered from south to north"""
    return 0

def normalize_grid(lon:list[float], lat:list[float]):
    newlons = normalize_lons(lon)
    newlats = normalize_lats(lat)
    return newlons, newlats


if __name__ == "__main__":
    lon = [float(x) for x in range(0,360,10)]
    lat = [float(y) for y in range(90,-90,-10)]
    print(f'lon = {lon}\nlat = {lat}')
    newlon, newlat = normalize_grid(lon, lat)
    print(f'newlon = {newlon}\nnewlat = {newlat}')
    