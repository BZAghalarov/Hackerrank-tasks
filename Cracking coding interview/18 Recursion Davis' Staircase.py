
'''

https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem
'''

'''

dict = {0:0, 1:1, 2:2, 3:4}

def steps(n):
    if n in dict.keys():
        return dict.get(n)
    result = steps(n-3) + steps(n-2) + steps(n-1)
    dict.update({n: result})
    return dict.get(n)
    
'''

#!/bin/python3


def countWays(n):
    res = [0] * (n + 1)
    res[0] = 1
    res[1] = 1

    for i in range(3, n + 1):
        if n > 2:
            res[2] = 2
        res[i] = res[i - 1] + res[i - 2] + res[i - 3]

    return res[n]


if __name__ == '__main__':
    s = int(input())

    for s_itr in range(s):
        n = int(input())

        print(countWays(n))