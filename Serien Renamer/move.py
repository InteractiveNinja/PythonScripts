import os
from os import listdir
from os.path import isfile, join

namingformat = open("name.txt","r").read()

onlyfiles = [f for f in listdir(".") if (isfile(join(".", f)) and (".mp4" in f)) ]
for t in onlyfiles:
    number  = [int(s) for s in t if s.isdigit()]
    numberarr = []
    print(len(number))
    if(len(number) > 3):
        numberarr.append(str(number[0]) + "" + str(number[1]))
        numberarr.append(str(number[2]) + "" + str(number[3]))
    else:
        numberarr.append("0" + str(number[0]))
        numberarr.append("0" + str(number[1]))
    os.rename(t,namingformat.format(numberarr[0],numberarr[1]))


