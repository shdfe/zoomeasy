from datetime import datetime

def get_closest(classes):
    return sorted(classes, key=lambda x: abs(x.start_time-datetime.now()))