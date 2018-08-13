
'''

https://www.hackerrank.com/challenges/torque-and-development/problem?h_l=playlist&slugs%5B%5D%5B%5D=interview&slugs%5B%5D%5B%5D=interview-preparation-kit&slugs%5B%5D%5B%5D=graphs

'''


#!/bin/python3

import sys

def Explore(city):
    global cost
    c = roads[city]
    for j in c:
        if cities[j] != 1:
            cities[j] = 1
            cost += y
            Explore(j)
q = int(input().strip())
for a0 in range(q):
    n,m,x,y = input().strip().split(' ')
    n,m,x,y = [int(n),int(m),int(x),int(y)]
    a = n+1
    roads = [[] for i in range(n+1)]
    cities = [0]*a
    for a1 in range(m):
        city_1,city_2 = input().strip().split(' ')
        city_1,city_2 = [int(city_1),int(city_2)]
        roads[city_1].append(city_2)
        roads[city_2].append(city_1)
    cost = 0
    if x < y:
        print(x*n)
        continue
    for i in range(1,a):
        if cities[i]!=1:
            cities[i] = 1
            cost += x
            Explore(i)
    print(cost)