
'''

https://www.hackerrank.com/challenges/ctci-big-o/problem?h_l=playlist&slugs%5B%5D%5B%5D=interview&slugs%5B%5D%5B%5D=interview-preparation-kit&slugs%5B%5D%5B%5D=miscellaneous

'''

'''

t = int(input())
for _ in range(t):
    n = int(input())
    print('Not prime' if sum([n%x==0 for x in range(2, int(n**(1/2))+1)]) or n==1 else 'Prime' )

'''

def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n%3==0 or n<2:
        return False
    i,w=5,2
    while i*i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True
for _ in range(int(input())):
    isprime = isPrime(int(input()))
    print("Prime" if isprime else "Not prime")