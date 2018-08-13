
'''

https://www.hackerrank.com/challenges/ctci-merge-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

'''

'''

def inversions(arr):
    n = len(arr)
    if n==1:
        return 0
    n1 = n/2
    n2 = n - n1
    arr1 = arr[:n1]
    arr2 = arr[n1:]
    ans = inversions(arr1) + inversions(arr2)
    i1 = 0
    i2 = 0
    for i in range(n):
        if i1 <n1 and (i2>=n2 or arr1[i1]<=arr2[i2]):
            arr[i] = arr1[i1]
            ans += i2
            i1 += 1
        elif i2 < n2:
            arr[i] = arr2[i2]
            i2 += 1
    return ans

for _ in range(input()):
    n = input()
    arr = map(int,raw_input().split())
    counts = inversions(arr)
    print counts

'''

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countInversions function below.
def merge(a1, a2):
    swaps, i, j, result, m, n = 0, 0, 0, [], len(a1), len(a2)
    ra = result.append
    while i < m and j < n:
        if a1[i] <= a2[j]:
            ra(a1[i])
            i += 1
        else:
            ra(a2[j])
            j += 1
            swaps += m - i
    result += a1[i:]
    result += a2[j:]
    return swaps, result


def msort(arr):
    n = len(arr)
    mid = n // 2
    if n > 1:
        left_swaps, left_result = msort(arr[:mid])
        right_swaps, right_result = msort(arr[mid:])
        m_swaps, result = merge(left_result, right_result)
        return m_swaps + left_swaps + right_swaps, result
    return 0, arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = msort(arr)

        fptr.write(str(result[0]) + '\n')

    fptr.close()
