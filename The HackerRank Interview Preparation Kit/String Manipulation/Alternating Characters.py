
'''

https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=playlist&slugs%5B%5D%5B%5D=interview&slugs%5B%5D%5B%5D=interview-preparation-kit&slugs%5B%5D%5B%5D=strings

'''

'''

t = input()
for _ in range(t):
    s = raw_input()
    count = 0
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count += 1
    print count
    
'''

#!/bin/python3

import sys


def alternatingCharacters(s):
    # Complete this function
    s=list(s)
    k=0
    for i in range(1,len(s)):
        if s[i] in ('A','B') or s[i-1] in ('A','B'):
            if s[i]==s[i-1]:
                k+=1


    return k

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = alternatingCharacters(s)
    print(result)
