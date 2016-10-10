def partition(ar):    
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
    output = ""
    for i in xrange(len(left)):
        output += str(left[i]) + " "
    for i in xrange(len(equal)):
        output += str(equal[i]) + " "
    for i in xrange(len(right)):
        output += str(right[i]) + " "
    print output

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)
