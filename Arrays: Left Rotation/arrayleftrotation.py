def array_left_rotation(a, n, k):
    for i in xrange(k):
        a.insert(n-1, a.pop(0))
    return a
  

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
