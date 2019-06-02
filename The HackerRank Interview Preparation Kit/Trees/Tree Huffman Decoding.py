
'''

https://www.hackerrank.com/challenges/tree-huffman-decoding/problem?h_l=playlist&slugs%5B%5D%5B%5D=interview&slugs%5B%5D%5B%5D=interview-preparation-kit&slugs%5B%5D%5B%5D=trees

'''

import queue as Queue

cntr = 0


class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None
        global cntr
        self._count = cntr
        cntr = cntr + 1

    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return self._count < other._count


def huffman_hidden():  # builds the tree and returns root
    q = Queue.PriorityQueue()

    for key in freq:
        q.put((freq[key], key, Node(freq[key], key)))

    while q.qsize() != 1:
        a = q.get()
        b = q.get()
        obj = Node(a[0] + b[0], '\0')
        obj.left = a[2]
        obj.right = b[2]
        q.put((obj.freq, obj.data, obj))

    root = q.get()
    root = root[2]  # contains root object
    return root


def dfs_hidden(obj, already):
    if (obj == None):
        return
    elif (obj.data != '\0'):
        code_hidden[obj.data] = already

    dfs_hidden(obj.right, already + "1")
    dfs_hidden(obj.left, already + "0")

"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""

'''

def is_leaf(node):
    return node.left is None and node.right is None

def decodeHuff(root , s):
    current = root
    result = []
    index = 0
    while index < len(s):
        while not is_leaf(current):
            if int(s[index]) > 0:
                current = current.right
            else:
                current = current.left
            index += 1
        result.append(current.data)
        current = root
    print(''.join(result))

'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root , s):
   #Enter Your Code Here
    temp=root
    string=[]
    for i in s:
        c=int(i)
        if c==1:
            temp=temp.right
        elif c==0:
            temp=temp.left
        if temp.right==None and temp.left==None:
            string.append(temp.data)
            temp=root
    b=''.join(string)
    print(b)

ip = input()
freq = {}#maps each character to its frequency

cntr = 0

for ch in ip:
    if(freq.get(ch) == None):
        freq[ch] = 1
    else:
        freq[ch]+=1

root = huffman_hidden()#contains root of huffman tree

code_hidden = {}#contains code for each object

dfs_hidden(root, "")

if len(code_hidden) == 1:#if there is only one character in the i/p
    for key in code_hidden:
        code_hidden[key] = "0"

toBeDecoded = ""

for ch in ip:
   toBeDecoded += code_hidden[ch]

decodeHuff(root, toBeDecoded)
