def is_matched(expression):
    expression = list(expression)
    openlist = ['[', '{', '(']
    closelist = [']','}', ')']
    closedict = {'[':']','{':'}','(':')'}
    balance = []
    if(expression[0] in closelist):
        return False
    while(len(expression) != 0):
        cur = expression.pop(0)
        if(cur in openlist):
            balance.append(cur)
        elif(len(balance)<=0):
            return False
        elif(cur in closelist):
            back = balance.pop()
            if(closedict[back] != cur):
                return False
    if len(balance) == 0:
        return True
    else:
        return False

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
