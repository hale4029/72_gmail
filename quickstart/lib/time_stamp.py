from datetime import datetime, timedelta
from dateutil.parser import parse

def UpdateTimeStamp():
    f = open("time_stamp.txt", "w")
    time = datetime.now()
    new_ts = time.strftime("%m/%d/%Y")
    f.write(new_ts)
    f.close()
    return new_ts

def PreviousTimeStamp():
    f = open("time_stamp.txt", "r")
    old_ts = f.read()
    old_ts = parse(old_ts)
    time = old_ts + timedelta(days=1)
    updated_ts = time.strftime("%m/%d/%Y")
    return updated_ts
