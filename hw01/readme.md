# Note

** Do not use python2 . You will have wrong encoding **



## First of all
We need to build a function that can read the html 

The homework wanted site:
[http://www.cwb.gov.tw/V7/observe/rainfall/A136.htm](http://www.cwb.gov.tw/V7/observe/rainfall/A136.htm)

In that html, 
we know that the data is the same as jquery  
``` jquery
	$("#tableData")
```

and we know the html table tree look like this
```
table
	thead
    	tr
        	th
            th
    tbody
    	tr
        	td
            td
        tr 
        	td
            td
    tfoot // we can ignore it
 ```
 
 Just use nested for to get the data
 
 Be careful for encoding


## Q1
	calculate rainfall of every country yesterday

I don't know what the question wanted 

So I output the country name and rainfall yesterday into file

## Q2 
	sort by rainfall and find the max and min rainfall

I think the key of rainfall is 24hours 

So i use build-in sorted to do that

and output as a file

## Q3
	check whether the statical is changed by time and update it
just use sleep to delay every minutes

** the demo answer output country but the statment say station ** 
In my opinion , I output the country name

## Q4
	Same as Q3 , but we can set certain observation station

If you want to set certain observation station's name, please place it at argv when you run my q4.py

you can use 測站 or 測站代碼  that both are accepted

## Q5
	use timestamp to update
just check it and update my data
