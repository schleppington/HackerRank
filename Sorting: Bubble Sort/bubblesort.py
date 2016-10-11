n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

totalSwaps = 0
for i in range(n):
    numberOfSwaps = 0
    
    for j in range(n-1):
        if(a[j] > a[j+1]):
            a[j], a[j+1] = a[j+1], a[j]
            numberOfSwaps += 1
    if(numberOfSwaps == 0):
        break
    totalSwaps += numberOfSwaps

print("Array is sorted in " + str(totalSwaps) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[n-1]))
