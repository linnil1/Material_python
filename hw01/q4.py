from get_rainfall import get_rainfall_data
import time
import sys

def print_rain (stations) :
    head,rainfall = get_rainfall_data("http://hw01:8000/A136.htm")

    chinese = ["測站(測站代碼)","1小時"]

    country = head.index(chinese[0])
    yesterday = head.index(chinese[1])

    rain_city = {}
    for i in rainfall :
        if any(st in i[country] for st in stations) :
            if i[yesterday][0].isdigit() : 
                #no good for transfer from str to float
                rain_city[i[country]] = "raining"
            else :
                rain_city[i[country]] = "no rain"

    print (rain_city)

while True:
    print_rain(sys.argv[1:])
    time.sleep(60) # every 1 minute ,check


