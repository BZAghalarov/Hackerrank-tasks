
'''

https://www.hackerrank.com/challenges/recursive-digit-sum/problem?h_l=playlist&slugs%5B%5D%5B%5D=interview&slugs%5B%5D%5B%5D=interview-preparation-kit&slugs%5B%5D%5B%5D=recursion-backtracking

'''


# !/bin/python3

def digitSum(n, k):
    x = sum(map(int, list(n)))
    if k == 1:
        return ds(x)
    else:
        return ds(x * k)


def ds(x):
    if x < 10:
        return x
    else:
        return ds(sum(map(int, list(str(x)))))


if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [str(n), int(k)]
    result = digitSum(n, k)
    print(result)
