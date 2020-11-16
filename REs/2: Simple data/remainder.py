import datetime

hour = datetime.datetime.now().hour + 8
minute = datetime.datetime.now().minute + 30

if minute >= 60:
    hour += 1
    minute -= 60

if hour > 24:
    hour -= 24

print("{}:{}".format(str(hour).zfill(2), str(minute).zfill(2)))
