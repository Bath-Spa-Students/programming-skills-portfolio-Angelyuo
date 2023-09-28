import time
clock = time.localtime()

hour = time.strftime("%H", clock)
minute = time.strftime("%M", clock)
second = time.strftime("%S", clock)

print("""TIME
      """) # For spacing

if int(hour) > 1:
    print("Hours:", hour)
elif int(hour) == 0:
    print("Hours:", hour)
else:
    print("Hour:", hour)
if int(minute) > 1:
    print("Minutes:", minute)
elif int(minute) == 0:
    print("Minutes:", minute)
else:
    print("Minute:", minute)
if int(second) > 1:
    print("Seconds:", second)
elif int(second) == 0:
    print("Seconds:", second)
else:
    print("Second:", second)
    
print("""
DATE      
""") # For spacing

year = time.strftime("%Y", clock)
month = time.strftime("%B", clock)
day = time.strftime("%d", clock)
print("Year:", year)
print("Month:", month)
print("Day:", day)