# HW02

## Question 1
請以 2016 年 4 月 2 日,分析國道五號塞車的狀況,須包含以下:	
A.	 請說明當天有塞車的路段	
B.	 哪些時段塞車,每次塞車持續多久	
(Hint:	 每兩分鐘記錄一次 , 只要比較第 n 筆與第 	 n+1	 筆的時間間隔 )	
C.	 找出塞車最低車速	
> note : time stramp should treat like this ` strftime('%s','2016-04-02') ` 
> 
> My output will be the duration and the lowest speed of every secontion where is jammed.
>
> **Attention : I think that traffic jam occur when it show twice at that moment**
>
> **And i think the interval of not continue traffic jam should be more than 10mins**
>
> I output on the screen also output to a Ans.db file
> 
> In the db file has a  
> ` TABLE jam (freewayname,mysection,myway,starttime real,endtime real,duration real,lowspeed int) `
>  
>  the meaning just same as its name 

> If you want to create one . just run ` python3 Q01.py `

## Question 2

請試著找出 2016 年 4 月 11 日到 4 月 15 日上班日,塞車最嚴重的路段	
(請以時速低 30km/hr 為主)	

> very easy
``` SQL
SELECT freewayname,mysection,myway,count(*) FROM lows    peed 
WHERE mytime BETWEEN strftime('%s',"2016-04-11") AND strftime('%s',"2016-04    -16") 
and myspeed < 30 
GROUP BY mysection
ORDER BY count(*) DESC 
  ```
> same as Q1 
> I output on the screen also output to a Ans.db file
> 
> In the db file has a  
> ` TABLE counting (freewayname,mysection,myway,time INT) `

> I think we need to output the Top X most serious traffic jam section  and it's occur time
> If you want to create one . just run ` python3 Q02.py `

## Question 3
  請以 2016 年農曆年假期間(2016 年 2 月 6 日至 2016 年 2 月 14 日),作答:	
A.	 請以各天為單位,將塞車的資料匯出為 CSV 檔,	
CSV 檔名的命名須為 ISO	Format,Ex:	2016 年 2 月 6 日,檔名為 20160206.csv	

B.	 請匯出 2016 年 2 月 9 日,上午時段(6:00-13:00)的資料,檔名為 20160209_AM.csv	

C.	 請分析年假期間,各個國道各個路段塞車排名(國道五號除外),並將結果匯出一 EXCEL
檔,輸出格式如下圖	 (Hint :找出每個國道持續塞車時段的數量 )	

> A B is  just output the data !! easy
>  Do you know that ? Excel not only can open .xls file but also .csv file . 
>  So , I don't want to output it as Excel and 
>  Do not use Excel . Please support LibreOffice , which is open-source and free. 
>  Unlike F**k Mirco$oft
  
  
> question C is just the same thing i di in question 2 XD  
> 
> i output as vacation.csv
> 
> If you want to create one . just run ` python3 Q03.py `
  
