
'''

https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

'''


#!/bin/python3



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
