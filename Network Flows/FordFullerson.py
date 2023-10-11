"""
adj_list
"""

from dataclasses import dataclass
from collections import deque

@dataclass
class EdgeInfo:
    frm: int
    to:int
    ind:int                                                 # id of this edge
    forward:bool

class Graph:
    def __init__(self,v):                                   # number of vertex
        self.adj_list=[[] for _ in range(v)]                # use adj_list to store the path
        self.flow= []
        self.c = []

    def addEdge(self, frm, to, capacity):
        self.adj_list[frm].append(EdgeInfo(frm,to,len(self.flow),True))
        self.adj_list[to].append(EdgeInfo(to,frm,len(self.flow),False))
        self.flow.append(0)                                                 # current flow on this edge is 0, add this in list flow
        self.c.append(capacity)                                             # add current c on list c
    
    def addFlow(self,edgeInfo,flow):                                        # increase flow or decrease flow on this edge
        if edgeInfo.forward:
            self.flow[edgeInfo.ind]+=flow
        else:
            self.flow[edgeInfo.ind]-=flow
    
    def traversable(self,edge):
        return self.left_over_capacity(edge) > 0
    
    def left_over_capacity(self,edge):
        if edge.forward:
            return self.c[edge.ind] - self.flow[edge.ind]
        else:
            return self.flow[edge.ind]
    
def bfs(g,n,source, sink):
    visited=[False for _ in range(n)]
    edge_taken = [None for _ in range(n)]           # current augmenting path 

    visited[source] = True
    q=[]
    q.append(source)
        
    while q:
        v = q.pop(0)
        for edge in g.adj_list[v]:
            if g.traversable(edge) and visited[edge.to]==False:
                visited[edge.to] = True
                edge_taken[edge.ind] = edge
                q.append(edge.to)
    if visited[sink]:                                           # if we meet the sink
        edge_used=[]
        node=sink                                               # we start from the sink
        while edge_taken[node]:
            edge_used.append(edge_taken[node])                  # track the augmenting path
            node= edge_taken[node].frm
        return edge_used
    return None

def edmond_karp(g,n,source,dest):
    while True:
        path = bfs(g,n,source,dest)
        if path is None:
            break
        flow = g.left_over_capacity(path[0])
        for edge in path:
            flow= min(flow,g.left_over_capacity(edge))
        for edge in path:
            g.add_flow(edge,flow)
    
    total_flow=0
    for edge in g.adj_list[source]:
        if edge.foward:
            total_flow+=g.flow[edge.ind]
    return total_flow


n,m = map(int,input().split()) 
g = Graph(n)
for _ in range(m):
    v,u,c = map(int, input().split())
    v -= 1
    u -= 1
    g.addEdge(v,u,c)

flow = edmond_karp(g,n,0,n-1)
print(flow)


