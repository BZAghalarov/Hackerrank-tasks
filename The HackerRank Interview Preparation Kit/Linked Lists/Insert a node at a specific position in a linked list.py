
'''

https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem?h_l=playlist&slugs%5B%5D%5B%5D=interview&slugs%5B%5D%5B%5D=interview-preparation-kit&slugs%5B%5D%5B%5D=linked-lists

'''

"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""


# This is a "method-only" submission.
# You only need to complete this method.
def InsertNth(head, data, position):
    pass


data = []
n = int(input())
for k in range(n):
    val = list(input().split(' '))
    data.insert(int(val[1]), int(val[0]))
print("".join(str(x) for x in data))






