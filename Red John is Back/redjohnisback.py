import math

def isPrime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number%i == 0:
            return False
    return True

def getPrimes(max):
    count=0
    for i in range(2, max+1):
        if isPrime(i): count+=1
    return count

t = int(raw_input().strip())

for j in xrange(t):
    n = int(raw_input().strip())
    arr=[0]*(n+1)
    arr[0]=1
    for i in xrange(1, n+1):
        if i>=4:
            arr[i]=arr[i-1]+arr[i-4]
        else:
            arr[i]=arr[i-1]
    print getPrimes(arr[n])
