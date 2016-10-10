#!/bin/python

import sys


time = raw_input().strip()
ampm = time[len(time)-2:]
timearr = time.split(':')

hours = timearr[0]
minutes = timearr[1]
seconds = timearr[2][:2]

if(ampm=="PM" and hours != "12"):
    hours = str(int(hours) + 12)
elif(ampm=="AM" and hours == "12"):
    hours = "00"
    

    
print(hours + ":" + minutes + ":" + seconds)
