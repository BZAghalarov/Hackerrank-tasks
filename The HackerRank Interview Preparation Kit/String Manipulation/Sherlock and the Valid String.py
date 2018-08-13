
'''

https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=playlist&slugs%5B%5D%5B%5D=interview&slugs%5B%5D%5B%5D=interview-preparation-kit&slugs%5B%5D%5B%5D=strings

'''

import sys
import collections


def isValid(s):
    c = collections.Counter(collections.Counter(s).values())
    if len(c) <= 1:
        return "YES"
    if len(c) == 2:
        curr = list(c)
        if abs(curr[0] - curr[1]) == 1:
            if c[max(curr[0], curr[1])] == 1:
                return "YES"
        if min(curr[0], curr[1]) == 1 and c[min(curr[0], curr[1])] == 1:
            return "YES"
    return "NO"


s = input().strip()
result = isValid(s)
print(result)