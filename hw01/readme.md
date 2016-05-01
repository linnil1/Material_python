# Note

** Do not use python2 . You will have wrong encoding **



## First of all
we need to build a function that can read the html 

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



