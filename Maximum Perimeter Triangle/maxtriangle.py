n = int(raw_input().strip())
arr = map(int, raw_input().strip().split())

if(n<3 or n>50):
    print -1
else:
    arr.sort()
    triangle = [0,0,0]
    for i  in xrange(n):
        if(triangle[0]+triangle[1]>triangle[2]):
            print(str(triangle[0])+" "+str(triangle[1])+" "+str(triangle[2]))
            break
        elif(i+3>len(arr)):
            print -1
            break
        else:
             triangle = arr[n-3-i:]
