
'''

https://www.hackerrank.com/challenges/ctci-coin-change/problem

'''

'''

#!/bin/python3

# Complete the ways function below.
def ways(n, coins):
    # Complete this function
    n_perms = [1]+[0]*n
    for coin in coins:
        for i in range(coin, n+1):
            n_perms[i] += n_perms[i-coin]
    return n_perms[n]

if __name__ == '__main__':
    n, m = map(int,input().split())
    coins = list(map(int, input().rstrip().split()))
    res = ways(n, coins)
    print(res)
    
'''

# !/bin/python3

import sys

def make_change(S, m, n):
    # We need n+1 rows as the table is constructed
    # in bottom up manner using the base case 0 value
    # case (n = 0)
    table = [[0 for x in range(m)] for x in range( n +1)]

    # Fill the entries for 0 value case (n = 0)
    for i in range(m):
        table[0][i] = 1

    # Fill rest of the table entries in bottom up manner
    for i in range(1, n+ 1):
        for j in range(m):
            # Count of solutions including S[j]
            x = table[i - S[j]][j] if i - S[j] >= 0 else 0

            # Count of solutions excluding S[j]
            y = table[i][j - 1] if j >= 1 else 0

            # total count
            table[i][j] = x + y

    return table[n][m - 1]


n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
print(make_change(coins, m, n))
