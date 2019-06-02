
'''

https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem?h_l=playlist&slugs%5B%5D%5B%5D=interview&slugs%5B%5D%5B%5D=interview-preparation-kit&slugs%5B%5D%5B%5D=recursion-backtracking

'''

def fibonacci(n):
    # Write your code here.
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
n = int(input())
print(fibonacci(n))
