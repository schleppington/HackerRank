#!/bin/python
def quick_sort(ar):
    if(len(ar)<=1):
        return ar
    p = ar[0]
    left = []
    right = []
    equal = []
    equal.append(p)
    for i in xrange(1, len(ar)):
        if(ar[i]>p):
            right.append(ar[i])
        elif(ar[i]<p):
            left.append(ar[i])
        else:
            equal.append(ar[i])
            
    ar = quick_sort(left) + equal + quick_sort(right)
    output = ""
    for i in xrange(len(ar)):
        output += str(ar[i]) + " "
    print output
    return ar

m = input()
ar = [int(i) for i in raw_input().strip().split()]
quick_sort(ar)
