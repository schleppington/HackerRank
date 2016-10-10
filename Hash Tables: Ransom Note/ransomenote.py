def ransom_note(magazine, ransom):
    zeros = [0]*len(list(magazine))
    mag = dict(zip(magazine, zeros))
    zeros = [0]*len(list(ransom))
    ran = dict(zip(ransom, zeros))
    for i in ransom:
        ran[i] = ran[i]+1
    for i in magazine:
        mag[i] = mag[i]+1
    for i in ransom:
        if i not in mag:
            return False
        elif ran[i]>mag[i]:
            return False
    return True

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
