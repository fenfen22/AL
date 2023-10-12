

"""
Scaling Algorithm:
Based on edmond_karp algorithm, we introduce a scaling parameter \deta
Only consider edges with capacity at least \deta in current residual graph
Start with \deta = "highest power of 2 <= largest capacity out of s"
When no more augmenting paths in current residual graph, we half \deta 
Stop when no more augmenting paths in residual graph, whose \deta is 1.
"""

import sys
from dataclasses import dataclass



@dataclass
class EdgeInfo:
    frm:int
    to:int
    ind:int                                                                 # id of this edge
    forward:bool

class DSGraph():                                                            # residual graph
    def __init__(self,n):
        self.adj_list = [[] for _ in range(n)]
        self.flow = []
        self.c = []
        self.deta = None
    

    def add_edge(self,frm,to,capacity):                                     # store this edge information in the residual graph
        self.adj_list[frm].append(EdgeInfo(frm, to, len(self.flow),True))
        self.adj_list[to].append(EdgeInfo(to, frm, len(self.flow),False))
        self.flow.append(0)
        self.c.append(capacity)
        

    def add_flow(self,edge,flow):
        if edge.forward:
            self.flow[edge.ind]+=flow
        else:
            self.flow[edge.ind]-=flow

    def traversable_deta(self,edge):
        return self.left_over_capacity(edge) >= self.deta                   # we only consider edges with capacity at least current deta
        
    def traversable(self,edge):
        return self.left_over_capacity(edge) > 0

    def left_over_capacity(self,edge):
        if edge.forward:
            return self.c[edge.ind]- self.flow[edge.ind]
        else:
            return self.flow[edge.ind]
    
    def get_deta(self,source):                                              # initial deta
        capacity = 0
        for edge in self.adj_list[source]:
            capacity = max(capacity,self.c[edge.ind])

        power = 0
        while 2**power <= capacity:
            power += 1
        self.deta = 2**(power-1)
        return self.deta

    def half_deta(self,deta):                                               # half deta
        self.deta = deta/2
        return self.deta

    

def bfs(g,n,source,sink):
    visited = [False for _ in range(n)]
    edge_taken = [None for _ in range(n)]

    queue = []
    visited[source]= True
    queue.append(source)

    while queue:
        v = queue.pop(0)
        for edge in g.adj_list[v]:
            if g.traversable_deta(edge) and visited[edge.to]==False:
                edge_taken[edge.to] = edge
                visited[edge.to]=True
                queue.append(edge.to)
    if visited[sink]:
        edge_used = []
        node = sink
        while edge_taken[node]:
            edge_used.append(edge_taken[node])
            node = edge_taken[node].frm
        return edge_used
    return None


# we start from s side, track all nodes that we could reach
def get_minimumCut_s(g,source):
    visited = [False for _ in range(n)]
    edge_taken = [None for _ in range(n)]

    queue = []
    visited[source]= True
    queue.append(source)

    while queue:
        v = queue.pop(0)
        for edge in g.adj_list[v]:
            if g.traversable(edge) and visited[edge.to]==False:
                edge_taken[edge.to] = edge
                visited[edge.to]=True
                queue.append(edge.to)
    vertex_used = []
    for i,vertex in enumerate(visited):
        if vertex == True:
            vertex_used.append(i+1)
    return vertex_used

def scaling_algorithm(g,n,source,sink):
    deta = g.get_deta(0)                                        # get the initial deta based on the largest capacity out of s
    while deta >= 1:
        path = bfs(g,n,source,sink)
        if path is None:                                        # if we could not get a path with current deta, we try to half current deta and continue
            deta = g.half_deta(deta)
        else:
            flow = g.left_over_capacity(path[0])
            for edge in path:
                flow = min(flow, g.left_over_capacity(edge))
            for edge in path:
                g.add_flow(edge,flow)
    total_flow = 0
    for edge in g.adj_list[source]:
        if edge.forward:
            total_flow += g.flow[edge.ind]
    return total_flow  




n,m = map(int,input().split())
g=DSGraph(n)

for _ in range(m):
    frm,to,c = map(int,input().split())
    frm-=1
    to-=1
    g.add_edge(frm,to,c)

print("maximum flow of this graph is :", scaling_algorithm(g,n,0,n-1))

print("minimun cut of s side is :", get_minimumCut_s(g,0))




