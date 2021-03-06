class MyQueue(object):
    def __init__(self):
        self.inbox = []
        self.outbox = []
    
    def peek(self):
        return self.inbox[0]
        
    def pop(self):
        if(len(self.inbox)>0):
            return self.inbox.pop(0)
        else:
            return None
        
    def put(self, value):
        self.inbox.append(value)

queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())
    
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()
