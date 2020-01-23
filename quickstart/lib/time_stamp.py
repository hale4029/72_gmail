import datetime
from dateutil.parser import parse

def UpdateTimeStamp():
    f = open("time_stamp.txt", "w")
    new_ts = str(datetime.datetime.now())
    f.write(new_ts)
    f.close()
    return new_ts

def PreviousTimeStamp():
    f = open("time_stamp.txt", "r")
    old_ts = f.read()
    old_ts = parse(old_ts)
    updated_ts = old_ts + datetime.timedelta(minutes=1)
    return updated_ts
