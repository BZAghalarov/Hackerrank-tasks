
'''

https://www.hackerrank.com/challenges/balanced-brackets/problem?h_l=playlist&slugs%5B%5D%5B%5D=interview&slugs%5B%5D%5B%5D=interview-preparation-kit&slugs%5B%5D%5B%5D=stacks-queues

'''


#!/bin/python3

class ArrayStack:
    '''LIFO Stack implementing using a Python list as underlying storage '''

    def __init__(self):
        '''Create an empty stack'''
        self._data = [] # nonpublic list instance

    def __len__(self):
        '''Return the number of elements in the stack'''
        return len(self._data)

    def is_empty(self):
        '''Return True if the stack is empty.'''
        return len(self._data)==0

    def push(self, e):
        '''Add element e to the top of the stack.'''
        self._data.append(e) # new item stored at end of list

    def top(self):
        ''' Return (but do not remove) teh element at the top of the stack.
            Raise Empty exception if the stack is empty.
        '''
        if self.is_empty():
            raise ('Stack is empty!')
        return self._data[-1] # the last item in the list

    def pop(self):
        '''Remove and return the element from the top of the stack (i.e LIFO)
            Raise Empty exception if the stack empty.
        '''

        if self.is_empty():
            raise ('Stack is empty')
        return self._data.pop() #remove last item from list

def isBalanced(expr):
    '''Return True if all delimiters are properly match.false otherwise'''
    lefty = '({['  # opening delimiters
    righty = ')}]'  # respective closing delimiters
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)  # push left delimiter on Stack
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False  # mismatched
    return S.is_empty()  # were all symbols matched

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        s = input().strip()
        result = isBalanced(s)
        if result == True:
            print('YES')
        else:
            print('NO')