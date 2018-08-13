
'''

https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=playlist&slugs%5B%5D%5B%5D=interview&slugs%5B%5D%5B%5D=interview-preparation-kit&slugs%5B%5D%5B%5D=dictionaries-hashmaps

'''




from collections import Counter


def ransom_note(magazine, rasom):
    l = Counter(rasom)
    k = Counter(magazine)
    j = Counter(rasom) - Counter(magazine)
    return (Counter(rasom) - Counter(magazine)) == {}


m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if (answer):
    print("Yes")
else:
    print("No")

