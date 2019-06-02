
'''

https://www.hackerrank.com/challenges/triple-sum/problem?h_l=playlist&slugs%5B%5D%5B%5D=interview&slugs%5B%5D%5B%5D=interview-preparation-kit&slugs%5B%5D%5B%5D=search


Sample Input 1

    3 3 3
    1 4 5
    2 3 3
    1 2 3

Sample Output 1

    5 

'''

def triplets(arra, arrb, arrc):
    x = 0
    y = 0
    z = 0
    cnt = 0
    res = {}
    d= {}
    '''
    p >> a
    p <= q
    
    q >> b
    r >> c
    q >= r
    
    '''
    arra = sorted(arra)
    arrb = sorted(arrb)
    arrc = sorted(arrc)
    while x < len(arra):
        if arra[x]<= arrb[y]:
            if arrb[y] >= arrc[z] and z < len(arrc):
                # aid olan pairleri yadda saxlayiriqki novbeti defe gelende onu yene saymiyaq
                d[cnt] = arra[x] , arrb[y] , arrc[z]
                if d[cnt].values not in res.values():
                    res[cnt] = arra[x] , arrb[y] , arrc[z]
                    cnt += 1
                    z += 1
                else:
                    z += 1

            else:
                if z < len(arrc):
                    z+=1
                elif y < len(arrb):
                    y += 1
                    z=0
                elif x < len(arra):
                    x += 1
                    y=0
                    z=0
        else:
            if y<len(arrb)-1:
                y+=1
                z=0
            else:
                if x< len(arra):
                    x += 1
                    y=0
                    z=0
        if z == len(arrc):
            z = 0
            y+=1
        if y == len(arrb):
            y = 0
            z=0
            x+=1
        if x == len(arra):
            break

    return cnt


lenaLenbLenc = input().split()

lena = int(lenaLenbLenc[0])

lenb = int(lenaLenbLenc[1])

lenc = int(lenaLenbLenc[2])

arra = list(map(int, input().rstrip().split()))

arrb = list(map(int, input().rstrip().split()))

arrc = list(map(int, input().rstrip().split()))

ans = triplets(arra, arrb, arrc)
print(ans)