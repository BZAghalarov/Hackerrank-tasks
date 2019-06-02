
'''

https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem


http://cslibrary.stanford.edu/110/BinaryTrees.html
https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/
https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/

https://www.geeksforgeeks.org/smallest-number-in-bst-which-is-greater-than-or-equal-to-n/

'''


import sys
def checkBST(root):
    if root is None:
        return True
    stack = [(float('-inf'), root, float('+inf'))]
    while stack:
        mind, node, maxd = stack.pop()
        if not (mind < node.data < maxd):
            return False
        if node.left is not None:
            stack.append((mind, node.left, node.data))
        if node.right is not None:
            stack.append((node.data, node.right, maxd))
    return True
def check(root, min, max):
    if root == None:
        return True
    if root.data <= min or root.data >= max:
        return False
    return check(root.left, min, root.data) and check(root.right, root.data, max)
def check_binary_search_tree_(root):
    return check(root, float('-inf'), float('inf'))