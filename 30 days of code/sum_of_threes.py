# Given a number n, return a string representing it as a sum of distinct powers of three, or return
# "Impossible" if that's not possible to achieve

# For n=4 the outut should be "3^1 + 3^0"
# 4 can be represented as 3+1 which is in fact 3 to the power of 1 plus 3 to the power of 0

# For n=2 the output should be impossible

from pprint import pprint as pp
import itertools
n= int(input())
stri=''
l=[]
d1 = {}
t=0
# loop verilen ededin listdeki sonuncu ededden kicik oldugu vaxta qeder davam edir
for i in range( 0, 100000 ):
    if n < pow(3,i):
        break
    l.append(pow(3,i))
    d1[pow(3,i)] = '3^' + str(i)

l0 = [list(c) for i in range(len(l)) for c in itertools.combinations(l,i+1) if sum(c)==n]

if not sum(l)<n:
    try:
        l1 = l0[0]
    except:
        l1=[]
    for key,value in d1.items():
        if key in l1:
            stri += str( value ) + ' + '
    s= stri[:-3]
else:
    s='Impossible'
print(s)

