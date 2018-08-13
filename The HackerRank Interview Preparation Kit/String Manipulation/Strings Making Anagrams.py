
'''

https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=playlist&slugs%5B%5D%5B%5D=interview&slugs%5B%5D%5B%5D=interview-preparation-kit&slugs%5B%5D%5B%5D=strings

'''


def number_needed(a, b):
    r=ca=cb=0
    for i in set(a):
        ca=a.count(i)
        if i in b:
            cb=b.count(i)
            r+= abs(ca - cb)
        else:
            r +=ca
    for i in set(b):
        cb=b.count(i)
        if i  not in a:
            r+= cb
    return r

a = input().strip()
b = input().strip()

print(number_needed(a, b))
