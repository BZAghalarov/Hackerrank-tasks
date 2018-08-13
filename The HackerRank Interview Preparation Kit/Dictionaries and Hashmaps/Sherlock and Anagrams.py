
'''

https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=playlist&slugs%5B%5D%5B%5D=interview&slugs%5B%5D%5B%5D=interview-preparation-kit&slugs%5B%5D%5B%5D=dictionaries-hashmaps

'''




from collections import *
for i in range(int(input())):
    s = input()
    check = defaultdict(int)
    l = len(s)
    for i in range(l):
        for j in range(i+1,l+1):
            sub = list(s[i:j])
            sub.sort()
            sub = "".join(sub)
            check[sub]+=1
    sum = 0
    for i in check:
        n = check[i]
        sum += (n*(n-1))/2
    print(sum)

'''

#!/bin/python3

import sys

from collections import Counter

def sherlockAndAnagrams(string):
    buckets = {}
    for i in range(len(string)):
        for j in range(1, len(string) - i + 1):
            key = frozenset(Counter(string[i:i+j]).items()) # O(N) time key extract
            buckets[key] = buckets.get(key, 0) + 1
    count = 0
    for key in buckets:
        count += buckets[key] * (buckets[key]-1) // 2
    return count



q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = sherlockAndAnagrams(s)
    print(result)

'''