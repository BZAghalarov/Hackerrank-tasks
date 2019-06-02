
'''

https://www.hackerrank.com/challenges/abbr/problem?h_l=playlist&slugs%5B%5D%5B%5D=interview&slugs%5B%5D%5B%5D=interview-preparation-kit&slugs%5B%5D%5B%5D=dynamic-programming

'''


def matchstring(a, b, store):
    if len(a) < len(b):
        return False

    dp = [True] + [False] * len(b)
    i = 0
    while i < len(b) and a[i].upper() == b[i]:
        i += 1
        dp[i] = True

    for i in range(len(a) - len(b)):
        dp[0] = dp[0] and a[i].islower()
        for j in range(len(b)):
            cha, chb = a[i + j + 1], b[j]
            if cha.isupper():
                dp[j + 1] = dp[j] and cha == chb
            elif cha.upper() == chb:
                dp[j + 1] = dp[j] or dp[j + 1]

    return dp[len(b)]


tt = int(input().strip())
for i in range(tt):
    s1 = input().strip()
    s2 = input().strip()
    store = [[-1 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
    abbr = matchstring(s1, s2, store)
    if not abbr:
        print("NO")
    else:
        print("YES")