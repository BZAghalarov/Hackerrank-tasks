
'''

https://www.hackerrank.com/challenges/pairs/problem?h_l=playlist&slugs%5B%5D%5B%5D=interview&slugs%5B%5D%5B%5D=interview-preparation-kit&slugs%5B%5D%5B%5D=search

Sample Input

    5 2  
    1 5 3 4 2  

Sample Output

    3

'''


# !/usr/bin/py
# Head ends here
def pairs(a, k):
    # a is the list of numbers and k is the difference value
    i = 0
    j = 1
    count = 0
    a=sorted(a)
    while j< len(a):
        diff = a[j] - a[i]
        if diff== k:
            count +=1
            j +=1
        elif diff > k:
            i+=1
        elif diff < k:
            j+=1

    answer = count
    return answer


# Tail starts here
if __name__ == '__main__':
    a = input().strip()
    a = list(map(int, a.split(' ')))
    _a_size = a[0]
    _k = a[1]
    b = input().strip()
    b = list(map(int, b.split(' ')))
    print(pairs(b, _k))