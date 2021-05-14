from datetime import datetime, timedelta
import calendar
import time

def get_closest(classes):
    return sorted(classes, key=lambda x: abs(x.start_time-datetime.now()))

def add_time(time): #Why is time so confusing
    utc_offset = 7
    # utc_offset = (calendar.timegm(time.gmtime())-calendar.timegm(time.localtime()))/60/60
    added = timedelta(hours=utc_offset)
    return time + added

def sort_by_oldest(classes):
    return sorted(classes, key=lambda x: x.start_time)