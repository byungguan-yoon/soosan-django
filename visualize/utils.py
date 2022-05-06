import datetime

def str2date(startdate, enddate):
    startdate = datetime.datetime.strptime(startdate, "%m/%d/%Y")
    startdate = startdate.replace(hour=0, minute=0)
    enddate = datetime.datetime.strptime(enddate, "%m/%d/%Y")
    enddate = enddate.replace(hour=23, minute=59)
    return startdate, enddate