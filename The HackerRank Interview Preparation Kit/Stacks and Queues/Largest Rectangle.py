
'''

https://www.hackerrank.com/challenges/largest-rectangle/problem?h_l=playlist&slugs%5B%5D%5B%5D=interview&slugs%5B%5D%5B%5D=interview-preparation-kit&slugs%5B%5D%5B%5D=stacks-queues

'''

import sys


def largestRectangle(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    stack = []
    largest = 0

    for i in range(len(heights)):
        h = heights[i]
        # k = heights[stack[-1][0]]
        if len(stack) == 0 or h > heights[stack[-1][0]]:
            stack.append((i, h))
        else:
            while len(stack) > 0 and heights[stack[-1][0]] > h:
                index, currArea = stack.pop()
                rightArea = (i - index - 1) * heights[index]
                largest = max(largest, currArea + rightArea)
            elemsLeft = (i - stack[-1][0]) if len(stack) > 0 else i + 1
            stack.append((i, elemsLeft * h))

    while len(stack) > 0:
        index, currArea = stack.pop()
        rightArea = (len(heights) - index - 1) * heights[index]
        largest = max(largest, currArea + rightArea)

    return largest


if __name__ == "__main__":
    n = int(input().strip())
    h = list(map(int, input().strip().split(' ')))
    result = largestRectangle(h)
    print(result)
