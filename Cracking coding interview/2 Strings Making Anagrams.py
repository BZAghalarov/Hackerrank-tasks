
'''

https://www.hackerrank.com/challenges/ctci-making-anagrams/problem


'''

'''
a=list(input())
b=list(input())
print(a)
c= len([val for val in a if val in b])
k= (len(a)+ len(b)) -(c*2)
print(k) 

'''

a = list(input())
b = list(input())
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

print(r)