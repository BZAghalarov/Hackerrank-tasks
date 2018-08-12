
'''

https://stackoverflow.com/questions/1801391/what-is-the-best-algorithm-for-checking-if-a-number-is-prime

https://www.geeksforgeeks.org/primality-test-set-2-fermet-method/
https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/

'''


'''

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n == 1 or n % 2 == 0 or n % 3 == 0:
        return False
    k = 1
    while 6*k-1 <= int(n ** 0.5):
        if n % (6*k-1) == 0 or n % (6*k+1) == 0:
            return False
        k += 1
    return True

'''

t = int(input())
for _ in range(t):
    n = int(input())
    print('Not prime' if sum([n%x==0 for x in range(2, int(n**(1/2))+1)]) or n==1 else 'Prime' )