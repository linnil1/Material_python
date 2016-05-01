from get_rainfall import get_rainfall_data
import time

def print_rain () :
	head,rainfall = get_rainfall_data("http://hw01:8000/A136.htm")

    chinese = ["行政區","1小時"]

    country = head.index(chinese[0])
    yesterday = head.index(chinese[1])

    rain_city = {}
    for i in rainfall :
        if i[yesterday][0].isdigit() : #no good for transfer from str to float
            rain_city[i[country]] = float(i[yesterday])

    print (rain_city)

print (" raining ")
while True:
    print_rain()
    time.sleep(60) # every 1 minute ,check


