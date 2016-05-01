from get_rainfall import get_rainfall_data

head,rainfall = get_rainfall_data()

chinese = ["行政區","前一日"]

country = head.index(chinese[0])
yesterday = head.index(chinese[1])

import csv

with open("q1Ans.csv","w") as mycsv:
    writer = csv.writer(mycsv) 
    writer.writerow(chinese)
    for i in rainfall :
        writer.writerow([i[country],i[yesterday]]) 
