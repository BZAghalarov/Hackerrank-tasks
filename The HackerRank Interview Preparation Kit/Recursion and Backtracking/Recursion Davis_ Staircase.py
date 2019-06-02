
'''

https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem?h_l=playlist&slugs%5B%5D%5B%5D=interview&slugs%5B%5D%5B%5D=interview-preparation-kit&slugs%5B%5D%5B%5D=recursion-backtracking

'''



# !/bin/python3


def countWays(n) :
    res = [0] * (n + 1)
    res[0] = 1
    res[1] = 1


    for i in range(3, n + 1) :
        if n> 2:
            res[2] = 2
        res[i] = res[i - 1] + res[i - 2] + res[i - 3]

    return res[n]


if __name__ == '__main__':
    s = int(input())

    for s_itr in range(s):
        n = int(input())

        print(countWays(n))
