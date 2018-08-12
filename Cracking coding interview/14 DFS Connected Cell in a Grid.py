
'''

https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/problem

https://www.geeksforgeeks.org/find-number-of-islands/
https://www.geeksforgeeks.org/find-length-largest-region-boolean-matrix/

'''

'''

class QuickUnion:
    def __init__(self, n):
        self.id = list(range(n))
        self.size = [1 for _ in range(n)]
    
    def root(self, i):
        p = self.id[i]
        while (i != p):
            i = self.id[self.id[p]]
            i = p
            p = self.id[p]
        return i
    
    def union(self, i, j):
        ri = self.root(i)
        rj = self.root(j)
        
        if (ri == rj): return
        
        size_ri = self.size[ri]
        size_rj = self.size[rj]
        
        if (size_ri >= size_rj):
            self.id[rj] = ri
            self.size[ri] += size_rj
        else:
            self.id[ri] = rj
            self.size[rj] += size_ri
            
    def max_group(self):
        return max(self.size)
            
            
def getBiggestRegion(grid):
    rows = len(grid)
    cols = len(grid[0])
    qu = QuickUnion(rows * cols)
    
    for y in range(rows):
        for x in range(cols):
            if (grid[y][x] != 1):
                continue
            if (x < cols - 1):
                if (grid[y][x+1] == 1):
                    qu.union(y * cols + x, y * cols + x + 1)
                if (y < rows - 1) and (grid[y+1][x+1] == 1):
                    qu.union(y * cols + x, (y+1) * cols + x + 1)
            if (y < rows - 1):
                if (grid[y+1][x] == 1):
                    qu.union(y * cols + x, (y+1) * cols + x)
                if (x > 0) and (grid[y+1][x-1] == 1):
                    qu.union(y * cols + x, (y+1) * cols + x - 1)           
                    
    return qu.max_group()
    
'''

'''

class Node:
    def __init__(self, data):
        self.adyacents = dict()
        self.data = data   

class Graph:
    def __init__(self):
        self.nodes = dict()

    def add(self, data):
        self.nodes[data] = Node(data)
        
    def connect(self, n1, n2):
        self.nodes[n1].adyacents[n2] = self.nodes[n2]
        self.nodes[n2].adyacents[n1] = self.nodes[n1]
        
def getBiggestRegion(grid, m):
    g = Graph() 
    for i, v in enumerate(grid):
        for j, w in enumerate(v):
            poc = j+i*m
            if w == 1:
                g.add(poc)
                u, l, ul, ur = poc-m, poc-1, poc-1-m, poc-m+1
                
                if u >= 0 and grid[u//m][j] == 1:
                    g.connect(poc, u)
                if l >= 0 and l//m == poc//m and grid[l//m][l%m] == 1:
                    g.connect(poc, l)
                if ul >= 0 and ul//m == (poc//m)-1 and grid[ul//m][ul%m] == 1:
                    g.connect(poc, ul)
                if ur >= 0 and ur//m == (poc//m)-1 and grid[ur//m][ur%m] == 1:
                    g.connect(poc, ur)
                    
    max = 0
    visited = dict()

    for i, n in g.nodes.items():
        res = countClustersSize(n, visited)
        max = res if res > max else max
    return max
        
def countClustersSize(n, visited):
    if n.data in visited and visited[n.data]:
        return 0
    visited[n.data] = True
    res = 1
    for i, node in n.adyacents.items():
        res += countClustersSize(node, visited)
    return res

'''

'''

def getBiggestRegion(grid,m,n):
   def size(i,j):
      if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == 1:
         grid[i][j] = 0
         return 1 + sum(size(i2,j2) for i2 in range(i-1,i+2) for j2 in range(j-1,j+2))
      return 0
   return max(size(i,j) for i in range(n) for j in range(m))

'''

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maxRegion function below.
def dfs(grid, i, j):
    n, m = len(grid), len(grid[0])
    positions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                 (0, 1), (1, -1), (1, 0), (1, 1)]
    grid[i][j] = 0
    count = 1

    for pos in positions:
        if i + pos[0] in range(n) and j + pos[1] in range(m):
            if grid[i + pos[0]][j + pos[1]] == 1:
                count += dfs(grid, i + pos[0], j + pos[1])

    return count


def getBiggestRegion(grid):
    n, m = len(grid), len(grid[0])
    max_region_size = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                max_region_size = max(max_region_size, dfs(grid, i, j))

    return max_region_size


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = getBiggestRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()