import sys

b=[]
ct=0
n = int(input().strip())
b= list(bin(n)[2:])
if len(b) == 3:
    max = 1
else:
    max = 0

for i in b:
    if i == '1' :
        ct+=1
        if ct>max:
            max=ct
    else:
       ct = 0
print(max)

