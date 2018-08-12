'''

https://web.stanford.edu/class/cs9/sample_probs/TwoSum.pdf

https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem

'''




#!/bin/python3


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

for _ in range(int(input())):
	money=int(input())
	n=int(input())
	costlist=[int(x) for x in input().split()]
	costhash={}
	for i in range(n):
		costhash[costlist[i]]=costhash.get(costlist[i],"")+" "+str(i+1)
	for i in costlist:
		if money-i in costhash:
			indices1=costhash[i].split()
			indices2=costhash[money-i].split()
			if (money-i)==i:
				print(indices1[0],indices1[1])
				break
			else:
				print(indices1[0],indices2[0])
				break
				
'''

'''
def get_flavours(money,flavours):
    map = {}

    for pos in range(len(flavours)):
        cost = flavours[pos]
        compliment = money - cost
        if compliment in map:
            return str(flavours.index(compliment) + 1) + ' ' + str(pos + 1)
        else:
            map[cost] = compliment

'''

'''

def get_flavours(money,flavours):
    map = {}
    for pos, cost in enumerate(flavours):
        if cost in map:
            return str(map[cost]) + ' ' + str(pos + 1)
        else:
            map[money-cost] = pos + 1

t = int(input())

for t_itr in range(t):
    money = int(input())

    n = int(input())

    cost = list(map(int, input().rstrip().split()))

    print(get_flavours(money, cost ))
    
'''