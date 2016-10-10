#!/bin/python

import sys


n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))

zeroes = [0]*n
socks = dict(zip(list(set(c)), zeroes))

for i in c:
    socks[i] += 1
pairs = 0
for i in socks:
    pairs += socks[i]//2
print pairs
