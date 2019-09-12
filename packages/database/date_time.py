import time
from datetime import datetime

def dates():
	now = datetime.now()
	datee = now.strftime("%d-%m-%Y")
	return datee

def times():
    now = datetime.now()
    tm_string = now.strftime("%H:%M")
    t = time.strptime(tm_string, "%H:%M")
    timee = time.strftime( "%I:%M %p", t )
    return timee


