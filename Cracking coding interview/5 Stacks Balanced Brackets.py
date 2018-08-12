'''

https://www.hackerrank.com/challenges/ctci-balanced-brackets

'''


def is_matched(expression):
    stack = []
    pairs = {'{': '}', '[': ']', '(': ')'}
    for char in expression:
        if char in pairs.keys():
            stack.append(pairs[char])
        else:
            # You need to check if the stack is empty or not before
            # accessing the last element in it, otherwise you get
            # IndexError: list index out of range
            if stack == [] or char != stack[-1]:
                return False
            stack.pop()
    return (stack == [])
    
t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")

'''
def is_matched(expression):

    if len(expression)%2 != 0:
        return False
    s=int(len(expression) / 2)
    st = expression[s:]
    nd = expression[:s]
    nde=nd[::-1]
    g=[]
    for i in range(0,len(nde)):
        if nde[i] == '(':
            g.append(')')
        elif nde[i] == '[':
            g.append(']')
        elif nde[i]=='{':
            g.append('}')
    g1=''.join(g)

    if st==g1 :
        return True
    else:
        return False
'''

'''
def is_matched(expression):

    if len(expression)%2 != 0:
        return False
    s=int(len(expression) / 2)
    st = expression[s:]
    nd = expression[:s]
    nde=nd[::-1]
    g=[]
    for i in range(0,len(nde)):
        if nde[i] == '(':
            g.append(')')
        elif nde[i] == '[':
            g.append(']')
        elif nde[i]=='{':
            g.append('}')
    g1=''.join(g)

    if st==g1 :
        return True
'''

'''
from pythonds import Stack

def is_matched(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False



t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")

'''