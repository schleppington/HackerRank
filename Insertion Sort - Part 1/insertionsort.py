#!/bin/python
def insertionSort(ar):
    for i in xrange(len(ar)):
        x = ar[i]
        j=i-1
        while j>=0 and ar[j] > x:
            ar[j+1] = ar[j]
            j = j-1
            print_array(ar)
        ar[j+1]=x
    print_array(ar)
    return ""

def print_array(ar):
    output = ""
    for i in xrange(len(ar)):
        output+=str(ar[i])+" "
    print output

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
