"""
we have two group nodes, one group contains all red nodes, aother group contains all blue node.

Bipartite Graph: all edges have a red and a blue endpoint

Matching: a subset of edges (M) such that no edges in M share an endpoint

Maximum matching: matching of maximum cardinality

Application: 
planes to routes
jobs to workers/machines
"""

class BipartiteGraph():
    def __init__(self):
        self.leftSide = set()
        self.rightSide = set()
        self.adj_list = {}
    
    def add_leftSide(self,vertex):
        self.leftSide.add(vertex)
        self.adj_list[vertex] = set()
    
    def add_rightSide(self,vertex):
        self.rightSide.add(vertex)
        self.adj_list[vertex] = set()
    
    def addEdges(self, left, right):
        self.adj_list[left].add(right)







g = BipartiteGraph()
n,m,k = map(int, input().split())
for i in range(n):
    label = "l".join(i)
g.add_leftSide()
for _ in range(k):
    v1,v2 = int(input().split())
    g.addEdges(v1,v2)


