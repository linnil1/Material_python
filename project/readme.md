# simulate particle in the box

I use vpython , so it need to use on Windows or using Wine

the main file is init.py

Because It is cpu-comsuming,
so i divide it to initcal.py and initshow.py

and initcalc.py will produce csv file (no vpython function),
so i can run on workstation

initshow.py will show result on your window ( vpython)
**and continue the situation**
which is convince when we need to continue our work

the csv data is put on /tmp/pvnrt/ 


## use time
it takes about 9 hour and i found that the work station is one core so
i just use one thread to do that

real    473m10.369s

user    462m26.550s

sys     0m7.693s


