
'''

https://www.hackerrank.com/challenges/ctci-contacts/problem

'''

'''

# all letters, a, ab, abc, ..
def edge_ngram(contact):
    return [contact[0:idx] for idx in range(1, len(contact) + 1)]

contact_indices = {}
def add(contact):
    for token in edge_ngram(contact):
        contact_indices[token] =contact_indices.get(token, 0) + 1

def find(name):
    return contact_indices.get(name, 0)

n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == 'add':
        add(contact)
    elif op == 'find':
        print(find(contact))
        
'''

'''

from collections import Counter

def grams(contact):
    return [contact[:i] for i in range(1, len(contact)+1)]

counter = Counter()
n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == 'add':
        counter.update(grams(contact))
    elif op == 'find':
        print(counter.get(contact, 0))

'''

'''

from collections import defaultdict
from sys import stdin

# the whole stupid split suffix functionality
# is only here because very rare long words will screw memory
# consumption otherwise

class Node(object):
    def __init__(self):
        self.val = ''
        self.children = defaultdict(Node)
        self.num_usage = 0
    
    @property
    def is_whole_suffix(self):
        return self.num_usage == 1   
    
    @property
    def children_suffix(self):
        assert self.is_whole_suffix         # meaningful only for whole suffixes
        return self.val[1:]                 
    
    def split_suffix(self):
        assert self.is_whole_suffix         # meaningful only for whole suffixes
        child = self.children[self.val[1]]
        child.val = self.val[1:]
        child.num_usage += 1        
        
    def add(self, char):
        if self.is_whole_suffix:            # preserve memory by concatinating
            self.val += char                # characters in suffix  if the word
            return self                     # is used only once
        
        child = self.children[char]
        if child.is_whole_suffix and len(child.val) > 1:
            child.split_suffix()

        child.val = char
        child.num_usage += 1
        return child
    
    def get(self, char):
        assert self.has(char)               # because defaultdict is used
        return self.children[char]
    
    def has(self, char):
        return char in self.children
    
    def has_same_suffix(self, rest_partial):
        assert self.is_whole_suffix         # meaningful only for whole suffixes
        return self.children_suffix[:len(rest_partial)] == rest_partial
    
class Trie(object):
    def __init__(self):
        self.root = Node()
        
    def add(self, word):
        node = self.root
        for char in word:
            node = node.add(char)
    
    def find(self, partial):
        node = self.root
        for i, char in enumerate(partial):
            if node.is_whole_suffix:
                rest_partial = partial[i:]
                return int(node.has_same_suffix(rest_partial))
            if not node.has(char):
                return 0
            node = node.get(char)
        return node.num_usage

n = int(input().strip())
trie = Trie()
for a0 in range(n):
    op, contact = stdin.readline().strip().split()
    if   op == 'add':
        trie.add(contact)
    elif op == 'find':
        print( trie.find(contact))
        
'''