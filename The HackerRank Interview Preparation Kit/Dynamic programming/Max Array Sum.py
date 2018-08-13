
'''

https://www.hackerrank.com/challenges/max-array-sum/problem?h_l=playlist&slugs%5B%5D%5B%5D=interview&slugs%5B%5D%5B%5D=interview-preparation-kit&slugs%5B%5D%5B%5D=dynamic-programming

Sample Input 0

    5
    3 7 4 6 5

Sample Output 0

    13

'''


s = int(input())
arr = list(input().split())
# arr = list(map(int, input().rstrip().split()))

incl = 0
excl = 0
temp = 0

for i in range(len(arr)):
	temp = incl
	incl = max(int(arr[i]) + int(excl), int(temp))
	excl = temp
print( max(incl, excl))


