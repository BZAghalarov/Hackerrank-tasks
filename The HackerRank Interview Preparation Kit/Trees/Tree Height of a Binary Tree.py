
'''

https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem?h_l=playlist&slugs%5B%5D%5B%5D=interview&slugs%5B%5D%5B%5D=interview-preparation-kit&slugs%5B%5D%5B%5D=trees

'''

'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''


def height(root):
    if root == None:
        return -1
    else:
        return 1 + max(height(root.left), height(root.right))