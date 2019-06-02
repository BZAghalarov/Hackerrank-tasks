
'''

https://www.hackerrank.com/challenges/two-strings/problem?h_l=playlist&slugs%5B%5D%5B%5D=interview&slugs%5B%5D%5B%5D=interview-preparation-kit&slugs%5B%5D%5B%5D=dictionaries-hashmaps

https://www.geeksforgeeks.org/python-set-operations-union-intersection-difference-symmetric-difference/

'''



def twoStrings(s1, s2):
    # create sets of unique characters
    # and test for intersection
    d = set(s1)
    f = set(s2)
    k = set(s1) | set(s2)
    if set(s1)&set(s2):
        return "YES"
    else:
        return "NO"

'''

import sys

def twoStrings(s1, s2):
    # Complete this function
    for j in s1:
        if j in s2:
            c='YES'
            break
        else:
            c='NO'
    return c
'''
q = int(input().strip())
for a0 in range(q):
    s1 = input().strip()
    s2 = input().strip()
    result = twoStrings(s1, s2)
    print(result)
