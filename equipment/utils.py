# https://gist.github.com/erans/983821


def _convert_to_degress(value):
    """Helper function to convert the GPS coordinates stored in the EXIF to degress in float format"""
    d0 = value[0][0]
    d1 = value[0][1]
    d = float(d0) / float(d1)

    m0 = value[1][0]
    m1 = value[1][1]
    m = float(m0) / float(m1)

    s0 = value[2][0]
    s1 = value[2][1]
    s = float(s0) / float(s1)

    return d + (m / 60.0) + (s / 3600.0)


def get_lat_lon(gps_exif):
    """Returns the latitude and longitude, if available, from the provided exif_data"""
    lat = None
    lon = None

    gps_latitude = gps_exif.get('GPSLatitude', None)
    gps_latitude_ref = gps_exif.get('GPSLatitudeRef', None)
    gps_longitude = gps_exif.get('GPSLongitude', None)
    gps_longitude_ref = gps_exif.get('GPSLongitudeRef', None)

    if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
        lat = _convert_to_degress(gps_latitude)
        if gps_latitude_ref != "N":
            lat = 0 - lat

        lon = _convert_to_degress(gps_longitude)
        if gps_longitude_ref != "E":
            lon = 0 - lon

    return lat, lon
