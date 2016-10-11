#!/bin/python3

import sys


arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)

curSum = float('-inf')

for i in range(4):
    for j in range(4):
        tempsum = 0
        tempsum += arr[i][j] + arr[i][j+1] + arr[i][j+2]
        tempsum += arr[i+1][j+1]
        tempsum += arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        if tempsum > curSum:
            curSum = tempsum

print(curSum)
