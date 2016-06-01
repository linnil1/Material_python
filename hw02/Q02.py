import sqlite3
conn = sqlite3.connect('freeway_log_hw02.db')
cursor = conn.execute(''' SELECT freewayname,mysection,myway,count(*) FROM lowspeed 
    WHERE mytime BETWEEN strftime('%s',"2016-04-11") AND strftime('%s',"2016-04-16") 
    and myspeed < 30 
    GROUP BY mysection
    ORDER BY count(*) DESC ''')

ansdb = sqlite3.connect('Ans.db')
ansdb.execute("DROP   TABLE IF EXISTS counting")
ansdb.execute("CREATE TABLE counting(freewayname,mysection,myway,count INT)")

for row in cursor:
    print(row)
    ansdb.execute('INSERT INTO counting VALUES (?,?,?,?)',(row[0],row[1],row[2],row[3]))

ansdb.commit()
ansdb.close()
conn.close()
