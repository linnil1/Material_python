import sqlite3
conn = sqlite3.connect('freeway_log_hw02.db')
cursor = conn.execute('''SELECT * FROM lowspeed
    WHERE mytime BETWEEN strftime('%s','2016-04-02') AND strftime('%s','2016-04-03')
    ORDER BY mysection ,myway,freewayname,mytime''')

#mytime|freewayname|mysection|myway|myspeed
#     0           1         2     3       4


ansdb = sqlite3.connect('Q01.db')
ansdb.execute("DROP TABLE IF EXISTS jam")
ansdb.execute(''' CREATE TABLE jam (
        freewayname,mysection,myway,
        starttime real,endtime real,duration real,lowspeed int)''')
# freewayname , secontion,way,starttime,endtime,lowest speed
ans=[[0,0,0,0,0,0]]

for rowtuple in cursor:
    #i think the interval of traffic jam  should lower than ten minutes
    # and should not just show one time
    row = list(rowtuple)
    if ans[-1][0:3] == row[1:4] and row[0]-ans[-1][4]<= 600:
        ans[-1][4]=row[0]
        ans[-1][5] = min( ans[-1][5] , row[4])
    else:
        #new one
        ans.append(row[1:4])
        ans[-1].append(row[0])
        ans[-1].append(row[0])
        ans[-1].append(row[4])

ans[:] = [a for a in ans if a[4]-a[3]>1]

for a in ans:
    print("freewayname:{0} section:{1} way:{2} time:{3}~{4} duration:{5} lowestspeed:{6}".format(a[0],a[1],a[2],a[3],a[4],a[4]-a[3],a[5]))
    ansdb.execute('INSERT INTO jam VALUES (?,?,?,?,?,?,?)',(a[0],a[1],a[2],a[3],a[4],a[4]-a[3],a[5]))

ansdb.commit()
ansdb.close()
conn.close()
