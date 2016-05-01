#!/usr/bin/python3
# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup


def get_rainrall_data ( url= 'http://www.cwb.gov.tw/V7/observe/rainfall/A136.htm' ) :

    mypage = requests.get(url)
    mypage.encoding = 'utf8'
    soup = BeautifulSoup(mypage.text,"html.parser")

    #table =soup.select("#tableData")  this return type is not bs
    table = soup.find("table",{"id":"tableData"})
    rows = table.find_all("tr")
    #print (table)

#this is for head
    cols = rows[0].find_all("th")
    arr = []
    for col in cols:
        arr.append(col.get_text())
    print (arr)
    
#this is for data
    for row in rows:
        if row is None:
            continue
        cols = row.find_all("td")
        arr = []
        for col in cols:
            arr.append(col.get_text())
        if len(arr) <= 1:
            continue
        print (arr)


    #print (table)


get_rainrall_data()
