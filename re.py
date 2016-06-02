import os

homework = "hw02"
srcdir = "Material_python/"+homework
wantdir = "/ntu/homework/"+homework+"/b04507022/"

osdir= os.listdir(srcdir+"/")
print (osdir)

for i in osdir:
	if i.endswith(".py") and i[0]=='Q':
		os.system("cp "+srcdir+"/"+i+" "+wantdir+homework+"-{0:0>2}-b04507022.py".format(i[2]))
	else:
		os.system("cp "+srcdir+"/"+i+" "+wantdir+i)
