from functools import cmp_to_key
class Player:
    name = ""
    score = 0
    
    def __init__(self, n, s):
        self.name = n
        self.score = s
        
    def __repr__(self):
        return
        
    def comparator(a, b):
        if a.score == b.score:
            result = min(a.name, b.name)
            if result == a.name:
                return -1
            else:
                return 1
        if a.score > b.score:
            return -1
        return 1
