class Node:
    children = []
    completes = 0
    char = ''
    
    def __init__(self):
        self.children = []
        self.completes = 0
        self.char = ''
    
    def getChild(self, c):
        for i in self.children:
            if i.char == c:
                return i
        return None

def addContact(curNode, s):
    j = 0
    for i in s:
        newNode = curNode.getChild(i)
        if newNode is None:
            newNode = Node()
            newNode.char = i
            curNode.children.append(newNode)
            curNode = curNode.children[len(curNode.children)-1]
        else:
            curNode = newNode
        curNode.completes += 1
        j += 1

def findContacts(curNode, s):
    for i in s:
        newNode = curNode.getChild(i)
        if newNode is None:
            return 0
        curNode = newNode
        
    return curNode.completes
        
n = int(input().strip())
root = Node()

for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == "add":
        addContact(root, contact)
    elif op == "find":
        print(findContacts(root, contact))
