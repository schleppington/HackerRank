class Node:
    children = {}
    completes = 0
    
    def __init__(self):
        self.children = {}
        self.completes = 0

def addContact(curNode, s):
    for i in s:
        if i not in curNode.children:
            curNode.children[i] = Node()
            curNode = curNode.children[i]
        elif i in curNode.children:
            curNode = curNode.children[i]
        curNode.completes += 1

def findContacts(curNode, s):
    for i in s:
        if i not in curNode.children:
            return 0
        curNode = curNode.children[i]
        
    return curNode.completes
        
n = int(input().strip())
root = Node()

for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == "add":
        addContact(root, contact)
    elif op == "find":
        print(findContacts(root, contact))
    
