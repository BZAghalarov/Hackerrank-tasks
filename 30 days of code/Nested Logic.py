'''

2 tarix daxil olunur
kod yoxlayir eger:
eyni il aydirsa gun ferqlidirse gunlerin sayin vurur 15-e

9 6 2015
6 6 2015
45

31 12 2009
1 1 2010
0

'''

t1 = input().split()
t2 = input().split()
fine=0
if t1[2] == t2[2] or not (t1[1]==12 and t2[1]==1):
    if t1[1] == t2[1]:
        if t1[0] == t2[0]:
            fine=0
        else:
            fine= (int(t2[0]) - int(t1[0])) * 15
    else:
        fine= (int(t2[1])-int(t1[1])) *500
else:
    if abs( t1[2] - t2[2] ) ==1 and t1[1]==12 and t2[1]==1:

    fine = 10000
print (abs(fine))