def quick_sort(ar, low, high):
    count = 0
    if low<high:
        p, count = partition(ar, low, high)
        count += quick_sort(ar, low, p-1)
        count += quick_sort(ar, p+1, high)
    return count

def partition(ar, low, high):
    count = 0
    pivot = ar[high]
    i = low
    for j in xrange(low, high):
        if ar[j] <= pivot:
            ar[i], ar[j] = ar[j], ar[i]
            i = i+1
            count += 1
    ar[i], ar[high] = ar[high], ar[i]
    count += 1
    return i, count

def insertion_sort(ar):
    count =0
    for i in xrange(len(ar)):
        x = ar[i]
        j=i-1
        while j>=0 and ar[j] > x:
            ar[j+1] = ar[j]
            j = j-1
            count += 1
        ar[j+1]=x
    return count

def print_array(ar):
    output = ""
    for i in xrange(len(ar)):
        output+=str(ar[i])+" "
    print output

m = input()
ar = [int(i) for i in raw_input().strip().split()]
copy = ar[:]
quickcount = quick_sort(ar, 0, len(ar)-1)
insertioncount = insertion_sort(copy)
print insertioncount - quickcount
