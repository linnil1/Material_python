from get_rainfall import get_rainfall_data
import time
import sys

def print_rain () :
    head,rainfall = get_rainfall_data()

    chinese = ["測站(測站代碼)","1小時"]

    country = head.index(chinese[0])
    yesterday = head.index(chinese[1])

    rain_city = {}
    for i in rainfall :
        if i[yesterday][0].isdigit() : 
            #no good for transfer from str to float
            rain_city[i[country]] = float(i[yesterday])

    print (rain_city)

import requests
data_time = 0
def data_is_change():
    t = float(requests.get("http://hw01:8000/timestamp.htm").text.strip())
    global data_time
    if t != data_time:
        data_time = t
        return True
    return False

while True:
    if data_is_change() :
        print_rain()
