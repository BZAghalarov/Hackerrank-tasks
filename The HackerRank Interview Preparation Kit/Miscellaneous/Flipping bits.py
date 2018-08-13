
'''

https://www.hackerrank.com/challenges/flipping-bits/problem?h_l=playlist&slugs%5B%5D%5B%5D=interview&slugs%5B%5D%5B%5D=interview-preparation-kit&slugs%5B%5D%5B%5D=miscellaneous

'''

#!/bin/python3

import math
import os

# Complete the flippingBits function below.
def flippingBits(N):
    return math.pow(2,32) -1 - N

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        N = int(input())

        result = int(flippingBits(N))

        fptr.write(str(result) + '\n')

    fptr.close()
