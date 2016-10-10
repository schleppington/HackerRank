#!/bin/python

import sys


n,k,q = raw_input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = map(int,raw_input().strip().split(' '))
m = []
for a0 in xrange(q):
    m.append(int(raw_input().strip()))
    
for i in xrange(k):
    a.insert(0, a.pop())
    
for i in xrange(q):
    print a[m[i]]
