
'''

https://www.hackerrank.com/challenges/ctci-ransom-note/problem

'''

'''
def ransom_note(magazine, ransom):

    for i in set(ransom):
        if ransom.count(i) > magazine.count(i):
            a = False
            break
        else:
            a = True
    return a
'''

from collections import Counter

def ransom_note(magazine, rasom):
    return (Counter(rasom) - Counter(magazine)) == {}


m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if (answer):
    print("Yes")
else:
    print("No")

