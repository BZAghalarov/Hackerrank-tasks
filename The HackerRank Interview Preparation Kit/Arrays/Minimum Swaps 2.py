
'''

https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=playlist&slugs%5B%5D%5B%5D=interview&slugs%5B%5D%5B%5D=interview-preparation-kit&slugs%5B%5D%5B%5D=arrays

'''

#!/bin/python3

import math
import os


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
	swaps = 0
	index = 0

	while index < len(arr):
		element = arr[index]

		if element == index + 1:
			index+=1
			continue
		else:
			temp = arr[element-1]
			arr[index] = temp
			arr[element-1] = element
			swaps+=1
	return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
