
'''

https://www.hackerrank.com/challenges/candies/problem?h_l=playlist&slugs%5B%5D%5B%5D=interview&slugs%5B%5D%5B%5D=interview-preparation-kit&slugs%5B%5D%5B%5D=dynamic-programming

'''

#!/bin/python3

import sys

def candies(n, arr):
    # Complete this function
    k=[]
    count = 0
    k = [1] * n
    for i in range(1,n):
        if arr[i] > arr[i-1]:
            k[i] = k[i-1] + 1

    for j in range(n-2,-1,-1):
        if arr[j] > arr[j+1]:
            k[j]= max(k[j],k[j+1]+1)

    for i in range(n):
        count = count + k[i]

    return count

if __name__ == "__main__":
    n = int(input().strip())
    arr = []
    arr_i = 0
    for arr_i in range(n):
       arr_t = int(input().strip())
       arr.append(arr_t)
    result = candies(n, arr)
    print(result)

