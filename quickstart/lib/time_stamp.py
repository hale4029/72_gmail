from datetime import datetime, timedelta
from dateutil.parser import parse

def UpdateTimeStamp():
    f = open("C:/Email_scrypt/72_gmail-master/quickstart/lib/time_stamp.txt", "w")
    time = datetime.now()
    new_ts = time.strftime("%m/%d/%Y")
    f.write(new_ts)
    f.close()
    return new_ts

def PreviousTimeStamp():
    f = open("C:/Email_scrypt/72_gmail-master/quickstart/lib/time_stamp.txt", "r")
    old_ts = f.read()
    time = parse(old_ts)
    #time = old_ts + timedelta(days=1)
    updated_ts = time.strftime("%m/%d/%Y")
    return updated_ts
