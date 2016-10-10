#!/bin/python

import sys


a0,a1,a2 = raw_input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = raw_input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]

alice = 0
bob = 0
if(a0>b0):
    alice += 1
elif(a0<b0):
    bob += 1
if(a1>b1):
    alice += 1
elif(a1<b1):
    bob+= 1
if(a2>b2):
    alice += 1
elif(a2<b2):
    bob += 1
print(str(alice)+" "+str(bob))
