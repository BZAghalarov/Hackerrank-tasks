
'''

https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=sorting

'''


'''

#!/usr/bin/python

N,K = map(int, raw_input().strip().split())
assert 1 <= N <= 10**5 and 1 <= K <= 10**9
lis = map(int, raw_input().strip().split())
for toy in lis:
    assert 1 <= toy <= 10**5

lis.sort()

count = 0
for i in range(N-1):
    K -= lis[i]
    if K < 0:
        print count
        exit(0)
    else:
        count += 1

print count

'''

#!/bin/python3

import sys

def maximumToys(prices, k):
    # Complete this function
    prices = sorted(prices)
    count = 0
    for i in range(len(prices)):
        if k-prices[i]>=0:
            count +=1
            k=k-prices[i]
        else:
            break
    return count

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    prices = list(map(int, input().strip().split(' ')))
    result = maximumToys(prices, k)
    print(result)