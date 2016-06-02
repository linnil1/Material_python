import sqlite3
import csv
import re
conn = sqlite3.connect('freeway_log_hw02.db')


def timetodb(start,end):
    return  conn.execute(''' SELECT * FROM lowspeed 
    WHERE mytime BETWEEN strftime('%s','{0}') AND strftime('%s','{1}') 
    '''.format(start,end))

def special(start,end):
    return conn.execute(''' SELECT freewayname,mysection,myway,count(*) FROM lowspeed 
    WHERE mytime BETWEEN strftime('%s',"{0}") AND strftime('%s',"{1}") 
    AND freewayname != "freeway5"
    GROUP BY mysection
    ORDER BY freewayname,count(*) DESC 
    '''.format(start,end))

def mycsv(name,start,end,func):
    with open(name, "w") as csv_file:
        cursor = func(start,end)
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([re.match("\w+",head[0]).group(0) for head in cursor.description]) # write headers
        csv_writer.writerows(cursor)

for i in range(6,15):
    day = "{0:02}".format(i)
    mycsv("201602"+day+".csv","2016-02-"+day,"2016-02-"+"{0:02}".format(i+1),timetodb)
    mycsv("20160209_AM.csv","2016-02-09 06:00:00","2016-02-09 13:00:00",timetodb)
    mycsv("vacation.csv","2016-02-06","2016-02-15 ",special)

conn.close()
