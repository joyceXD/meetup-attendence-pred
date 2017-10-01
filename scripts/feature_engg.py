

def event_hour_transform(h_value):
    value = math.cos(2*math.pi*(h_value-6)/24)
    return value


def label_attendance(attend):
    if attend == 'yes' or attend == 'waitlist':
        return 1
    else:
        return 0


def lat_lon_similarity(lat1, lon1, lat2, lon2):
    lat_diff = lat1-lat2
    lon_diff = lon1-lon2
    sim = (lat_diff**2+lon_diff**2)**(0.5)
    return sim