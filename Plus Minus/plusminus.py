#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

pos = 0
neg = 0
zero = 0

for i in xrange(n):
    if(arr[i]>0):
        pos += 1
    elif(arr[i]<0):
        neg += 1
    else:
        zero += 1

print(float(pos)/n)
print(float(neg)/n)
print(float(zero)/n)
