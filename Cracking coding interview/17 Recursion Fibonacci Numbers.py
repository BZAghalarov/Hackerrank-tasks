
'''

mem = {}
def fibonacci(n):
    if n < 2:
        return n
    try:
        return mem[n]
    except:
        mem[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return mem[n]
        
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