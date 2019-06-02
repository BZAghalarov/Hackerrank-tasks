
'''

https://www.hackerrank.com/challenges/poisonous-plants/problem?h_l=playlist&slugs%5B%5D%5B%5D=interview&slugs%5B%5D%5B%5D=interview-preparation-kit&slugs%5B%5D%5B%5D=stacks-queues

'''

#!/bin/python3


import os


# Complete the poisonousPlants function below.
def poisonousPlants(p,n):
    days = [0] * n
    s = [0]
    mi = p[0]
    ma = 0
    for i in range(1, n):
        if p[i] > p[i - 1]:
            days[i] = 1
        mi = min(mi, p[i])
        while s and p[s[-1]] >= p[i]:
            if p[i] > mi:
                days[i] = max(days[i], days[s[-1]] + 1)
            s.pop()
        ma = max(ma, days[i])
        s += [i]
    return ma


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p,n)

    fptr.write(str(result) + '\n')

    fptr.close()
