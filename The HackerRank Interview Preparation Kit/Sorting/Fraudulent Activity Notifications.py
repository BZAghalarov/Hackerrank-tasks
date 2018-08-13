
'''

https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=playlist&slugs%5B%5D%5B%5D=interview&slugs%5B%5D%5B%5D=interview-preparation-kit&slugs%5B%5D%5B%5D=sorting

'''


'''

import sys
#sys.stdin = open("in", "r")
n, d = map(int, raw_input().split())
arr = map(int, raw_input().split())

dic = {}

def find(idx):
    s = 0
    for i in xrange(0, 200):
        freq = 0
        if i in dic:
            freq = dic[i]
        s = s + freq
        if s>=idx:
            return i
        
ans = 0
for i in xrange(0, n):
    val = arr[i]
    
    if i>=d:
        med=find(d/2 + d%2)
        
        if d%2==0:
            ret = find(d/2+1)
            if val >=med + ret:
                ans = ans+1
        else:
            if val>=med*2:
                ans = ans + 1

    if val not in dic: dic[val] = 0
    dic[val] = dic[val] + 1
    
    #print i,dic
    if i>=d:
        prev = arr[i-d]
        dic[prev] = dic[prev]-1

print ans

'''

import bisect

def find_median(n):
    input_list = []
    for row in n:
        bisect.insort_left(input_list, row)
    if len(input_list)%2 == 1:
        return input_list[len(input_list)//2]
    else:
        return (input_list[len(input_list)//2] + input_list[len(input_list)//2-1])/2.0

def fraud(input_list, d):
    counter = 0
    median_list = []
    if len(input_list) <= d:
        return counter
    else:
        for i, row in enumerate(input_list):
            if i >= d:
                if d % 2 == 1:
                    max_threshold = median_list[d//2]
                else:
                    max_threshold = (median_list[d//2 - 1] + median_list[d//2])/2.0
                if row >= 2 * max_threshold:
                    counter += 1
                del median_list[bisect.bisect_left(median_list, input_list[i-d])]
            bisect.insort_left(median_list, row)
    return counter

n, d = list(map(int, input().strip().split()))
input_list = list(map(int, input().strip().split()))
print (fraud(input_list, d))