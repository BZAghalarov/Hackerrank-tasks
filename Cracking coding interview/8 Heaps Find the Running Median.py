
'''

https://www.hackerrank.com/challenges/ctci-find-the-running-median/problem

https://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/

'''


from bisect import insort


def median(a):
    if len(a) % 2 == 0:
        l = a[len(a) // 2];
        r = a[(len(a) // 2) - 1]
        med = (l + r) / 2.0

    elif len(a) % 2 != 0:
        med = a[len(a) // 2]
    return med


if __name__ == '__main__':
    heap = []
    for _ in range(int(input())):
        insort(heap, int(input()))
        print(float(median(heap)))

'''

import sys
import heapq

n = int(input().strip())
a = []
min_heap = []
max_heap = []
len_min_heap = 0
len_max_heap = 0

a_i = 0
for a_i in range(n):
    a_t = int(input().strip())
    if a_i == 0:
        heapq.heappush(max_heap, -1*a_t)
        heapq.heappush(min_heap, a_t)
        print(float(a_t))
    elif a_i == 1:
        if a_t > min_heap[0]:
            heapq.heapreplace(min_heap, a_t)
        else:
            heapq.heapreplace(max_heap, -1*a_t)
        print((min_heap[0] - max_heap[0])/2)
        len_min_heap = 1
        len_max_heap = 1
    else:
        if len_min_heap == len_max_heap:
            if -1 * a_t < max_heap[0]:
                heapq.heappush(min_heap, a_t)
                len_min_heap += 1
                print(float(min_heap[0]))
            else:
                heapq.heappush(max_heap, -1*a_t)
                len_max_heap += 1
                print(float(-1 * max_heap[0]))
        elif len_min_heap > len_max_heap:
            if a_t > min_heap[0]:
                heapq.heappush(min_heap, a_t)
                heapq.heappush(max_heap, -1*heapq.heappop(min_heap))
            else:
                heapq.heappush(max_heap, -1*a_t)
            len_max_heap += 1
            print((min_heap[0]-max_heap[0])/2)
        else:
            if -1 * a_t > max_heap[0]:
                heapq.heappush(max_heap, -1 * a_t)
                heapq.heappush(min_heap, -1*heapq.heappop(max_heap))
            else:
                heapq.heappush(min_heap, a_t)
            len_min_heap += 1
            print((min_heap[0]-max_heap[0])/2)
             
    a.append(a_t)

'''


'''

import sys

def getMedian(L):
    middle = len(L)/2
    if len(L) % 2 == 0:
        return float((L[int(middle)] + L[int(middle) - 1]))/2
    else:
        return float(L[int(middle)])
    
def quickSortAdd(num, L):
    if len(L) == 0:
        return [num]
    if num < L[0]:
        return [num] + L
    elif num > L[-1]:
        return L + [num]
    i = binary_search(L, num)
    return L[:i] + [num] + L[i:]

def binary_search(array, target):
    lower = 0
    upper = len(array)
    while lower < upper:
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val or (target < val and target > array[x-1]):
            return x
        elif target > val:
            if lower == x:
                break
            lower = x
        elif target < val:
            upper = x


n = int(input().strip())
a = []
a_i = 0
for a_i in range(n):
    a_t = int(input().strip())
    a.append(a_t)
    
runningList = []
for num in a:
    runningList = quickSortAdd(num, runningList)
    print (getMedian(runningList))

'''