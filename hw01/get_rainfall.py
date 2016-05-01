#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


def get_rainfall_data ( url= 'http://www.cwb.gov.tw/V7/observe/rainfall/A136.htm' ) :

    mypage = requests.get(url)
    mypage.encoding = 'utf8'
    soup = BeautifulSoup(mypage.text,"html.parser")

    #table =soup.select("#tableData")  this return type is not bs
    table = soup.find("table",{"id":"tableData"})
    #print (table)


	#this is for head
    headarr = []
    cols = table.find_all("th")
    for col in cols:
        headarr.append(col.get_text())
    #print (tmparr)
	
	#this is for data
    arr     = []
    rows = table.find_all("tr")
    for row in rows:
        if row is None:
            continue
        cols = row.find_all("td")
        tmparr = []
        for col in cols:
            tmparr.append(col.get_text())
        if len(tmparr) <= 1:
            continue
        #print (tmparr)
        arr.append(tmparr)

    return headarr,arr
