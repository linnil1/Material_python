from get_rainfall import get_rainfall_data

head,rainfall = get_rainfall_data("http://hw01:8000/rainfall.htm")

chinese = ["行政區","24小時"]

country = head.index(chinese[0])
yesterday = head.index(chinese[1])

sorted(rainfall,key=lambda i:i[yesterday])

import csv

with open("q2Ans.csv","w") as mycsv:
    writer = csv.writer(mycsv) 
    writer.writerow(["most" ,rainfall[0][country],rainfall[0][yesterday]]) 
    writer.writerow(["least" ,rainfall[-1][country],rainfall[-1][yesterday]]) 
    head = ["rank"]
    head.extend(chinese)
    writer.writerow(head)
    rank = 0
    for i in rainfall :
        writer.writerow([rank,i[country],i[yesterday]]) 
        rank+=1
