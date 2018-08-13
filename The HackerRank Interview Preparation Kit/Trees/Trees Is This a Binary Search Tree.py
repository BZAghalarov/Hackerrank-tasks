
'''

https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem?h_l=playlist&slugs%5B%5D%5B%5D=interview&slugs%5B%5D%5B%5D=interview-preparation-kit&slugs%5B%5D%5B%5D=trees

'''

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


def checkBST(root):
    return (check_in_order(root, [-1]))


def check_in_order(root, prev):
    result = True
    if root.left is not None:
        result &= check_in_order(root.left, prev)
    if prev[0] >= root.data:
        return False
    prev[0] = root.data
    if root.right is not None:
        result &= check_in_order(root.right, prev)
    return result

