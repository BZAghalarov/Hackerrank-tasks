
'''

https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem?h_l=playlist&slugs%5B%5D%5B%5D=interview&slugs%5B%5D%5B%5D=interview-preparation-kit&slugs%5B%5D%5B%5D=search

https://web.stanford.edu/class/cs9/sample_probs/TwoSum.pdf

'''


'''

#!/bin/python3

import sys
from collections import defaultdict

def solve(arr, money):
    hashTable = defaultdict(lambda: [])
    for i in range(len(arr)):
        hashTable[arr[i]].append(i);
        
    for k in hashTable.keys():
        if (money - k) in hashTable.keys():
            result = [];
            result.append(hashTable[k][0]+1);
            if (k == (money - k)) and len(hashTable[money - k]) > 1:
                result.append(hashTable[money - k][1]+1)
            else:
                result.append(hashTable[money - k][0]+1)
            
            if len(result) == 2:
                print(" ".join(map(str,sorted(result))))
                break
        

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        money = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        solve(arr, money)

'''

'''

#!/bin/python3

import sys
import operator

def solve(arr, money):
    d = {i:a for i,a in enumerate(arr)}
    d = sorted(d.items(), key=operator.itemgetter(1))
    i=0
    j=len(arr)-1
    while d[i][1] + d[j][1] != money:
        i += (d[i][1] + d[j][1] < money)
        j -= (d[i][1] + d[j][1] > money)
    return sorted([d[i][0]+1, d[j][0]+1])

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        money = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        i, j = solve(arr, money)
        print(i, j)

'''

'''

dict={}
    for  i in range(len(arr)):
        if money-arr[i] in dict:
            print(dict[money-arr[i]],i+1)
        else:
            dict[arr[i]]=i+1

'''



t = int(input().strip())
for a0 in range(t):
    m = int(input().strip())
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    # find matched number
    cost_map = {}
    for i, cost in enumerate(a):
        sunny = cost
        johnny = m - cost
        if johnny in cost_map.keys():
            print (str(cost_map[johnny]+1) + ' ' + str(i+1))
        else:
            cost_map[cost] = i