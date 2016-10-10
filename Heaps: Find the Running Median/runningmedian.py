import heapq

def _heappush_max(heap, item):
    heap.append(item)
    heapq._siftdown_max(heap, 0, len(heap)-1)


def _heappop_max(heap):
    """Maxheap version of a heappop."""
    lastelt = heap.pop()  # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        heapq._siftup_max(heap, 0)
        return returnitem
    return lastelt

maxheap = []
minheap = []
n = int(input().strip())
heapq.heapify(minheap)
heapq._heapify_max(maxheap)
for i in range(n):
    x = int(input().strip())
    if len(maxheap)>0 and x < maxheap[0]:
        _heappush_max(maxheap, x)
    else:
        heapq.heappush(minheap, x)
    
    if abs(len(maxheap) - len(minheap)) > 1:
        if len(maxheap) > len(minheap):
            heapq.heappush(minheap, _heappop_max(maxheap))
        else:
            _heappush_max(maxheap, heapq.heappop(minheap))
    
    if len(maxheap) == len(minheap):
        print((maxheap[0]+minheap[0])/2)
    elif len(maxheap)>len(minheap):
        print(float(maxheap[0]))
    else:
        print(float(minheap[0]))

