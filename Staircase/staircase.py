#!/bin/python

import sys


n = int(raw_input().strip())

for i in xrange(n):
    output = ""
    for j in xrange(n):
        if(j>=n-i-1):
            output += "#"
        else:
            output += " "
    print output
