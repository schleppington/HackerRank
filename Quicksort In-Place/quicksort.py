def quick_sort(ar, low, high):
    if low<high:
        p = partition(ar, low, high)
        quick_sort(ar, low, p-1)
        quick_sort(ar, p+1, high)

def partition(ar, low, high):
    pivot = ar[high]
    i = low
    for j in xrange(low, high):
        if ar[j] <= pivot:
            ar[i], ar[j] = ar[j], ar[i]
            i = i+1
    ar[i], ar[high] = ar[high], ar[i]
    print_array(ar)
    return i

def print_array(ar):
    output = ""
    for i in xrange(len(ar)):
        output+=str(ar[i])+" "
    print output

m = input()
ar = [int(i) for i in raw_input().strip().split()]
quick_sort(ar, 0, len(ar)-1)
