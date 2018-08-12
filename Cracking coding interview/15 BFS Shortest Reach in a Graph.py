'''

https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem?h_r=next-challenge&h_v=zen

https://www.youtube.com/watch?v=zaBhtODEL0w
https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/


'''

'''

from collections import deque

class Graph():
    def __init__(self, node_count):
        self.nodes = {}
        for i in range(node_count):
            self.nodes[i] = []

    def connect(self, a, b):
        self.nodes[a].append(b)
        self.nodes[b].append(a)

    def find_all_distances(self, label):
        original_label = label
        distance = 0
        paths = {}
        q = deque([(label, distance, self.nodes[label])])

        while(q):
            label, distance, neighbors = q.popleft()
            if label not in paths: # Prevent cycles
                paths[label] = distance
                for neighbor in neighbors:
                    q.append((neighbor, distance + 6, self.nodes[neighbor]))

        # Set unreachable nodes to -1 distance
        for node in self.nodes:
            if node not in paths:
                paths[node] = -1
        del paths[original_label] # node should not have a path to itself
return [paths[node] for node in paths]

'''

'''

import heapq
import queue

class Graph:
    def __init__(self, n):
        self.num = n
        self.nodes = {}
        for i in range(1, n+1):
            self.nodes[str(i)] = []

    def connect(self, x, y):
        self.nodes[str(x)].append(y)
        self.nodes[str(y)].append(x)

    def findnode(self, s, t):
        Q = []
        visited = set()

        heapq.heappush(Q, (0, s))
        while Q:
            f, cand = heapq.heappop(Q)
            # connect before you append to queue
            if cand == t:
                return f
            if cand in visited:
                continue
                
            visited.add(cand)
            for child in self.nodes[str(cand)]:
                if cand == child :
                    continue
                else:
                    # Fresh Node
                    newf = f + 6
                    heapq.heappush(Q, (newf, child))
        return -1

    def find_all_distances(self, s):
        dist = []
        for i in range(1, n+1):
            if i == s:
                continue
            print(self.findnode(s, i), end = " ")
        print("")



t = int(input())

for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x,y)
    s = int(input())
    graph.find_all_distances(s)
    
'''

import queue
from collections import defaultdict

class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = defaultdict(lambda: [])

    def connect(self,x,y):
        self.edges[x].append(y)
        self.edges[y].append(x)

    def find_all_distances(self, root):
        distances = [-1 for i in range(self.n)]
        unvisited = set([i for i in range(self.n)])
        q = queue.Queue()

        distances[root] = 0
        unvisited.remove(root)
        q.put(root)

        while not q.empty():
            node = q.get()
            children = self.edges[node]
            height = distances[node]
            for child in children:
                if child in unvisited:
                    distances[child] = height + 6
                    unvisited.remove(child)
                    q.put(child)

        distances.pop(root)

        print(" ".join(map(str,distances)))

t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1)
    s = int(input())
    graph.find_all_distances(s-1)