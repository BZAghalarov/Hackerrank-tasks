'''


https://www.geeksforgeeks.org/bubble-sort/
https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

'''

'''
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

numSwaps = 0

while True:
    SwapsFlag = False
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            numSwaps += 1
            SwapsFlag = True
    if not SwapsFlag:
        break


print('Array is sorted in', numSwaps, 'swaps.')
print('First Element:', a[0])
print('Last Element:', a[-1])

'''

'''

def bubble_sort(numList):
    numSwaps = 0
    sortList = numList
    
    def check(lst):
        return sorted(lst) == lst
    
    while not check(sortList):
        for i in range(len(numList)-1):
            if sortList[i] > sortList[i+1]:
                sortList[i], sortList[i+1] = sortList[i+1], sortList[i]
                numSwaps += 1
    
    print('Array is sorted in {} swaps.'.format(numSwaps))
    print('First Element: {}'.format(sortList[0]))
    print('Last Element: {}'.format(sortList[-1]))
    
'''

'''

def bubble_sort(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                count = count + 1
    return count, arr


n = int(input())
arr = list(map(int, input().split()))
count, arr = bubble_sort(arr)
print("Array is sorted in " + str(count) + " swaps.")
print("First Element: " + str(arr[0]))
print("Last Element: " + str(arr[-1]))

'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(arr):
    k = len(arr)
    cnt_op = 0
    for i in range(k):
        for j in range(k-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                cnt_op +=1
    print('Array is sorted in '+ str(cnt_op)+ ' swaps.')
    print('First Element: ' + str(arr[0]))
    print('Last Element: ' + str(arr[len(arr)-1]))

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)

