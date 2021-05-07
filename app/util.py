from datetime import datetime
import datetime as dt

def get_closest(classes):
    return sorted(classes, key=lambda x: abs(x.start_time-datetime.now()))

def add_time(time): #Why is time so confusing
    utc_offset = 7
    added = dt.timedelta(hours=utc_offset)
    return time + added