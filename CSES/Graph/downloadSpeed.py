from dataclasses import dataclass
from collections import deque

n,m = map(int,input().split())                                  # n is number of vertex, m is number of edges

@dataclass
class EdgeInfo:
    frm:int                                                     # vertex id of this edge points from
    to:int                                                      # vertex id of this edge points to
    ind:int                                                     # id of this edge start from 0
    foward:bool                                                 # direction of this edge

class FlowGraph:                                                # this is residual graph actually.
    def __init__(self,v):                                       # adj_list, list of flow and list of capacity
        self.adj_list = [[] for _ in range(v)]                  # adj_list for all vertex
        self.flow=[]                                            # store flows for all edges
        self.c = []                                             # store capacities for all edges


    # adj_list / list of flow / list of c
    def add_edge(self,frm,to,capacity):                         # add an edge(frm,to, capacity)
        self.adj_list[frm].append(EdgeInfo(frm, to, len(self.flow),True))
        self.adj_list[to].append(EdgeInfo(to, frm, len(self.flow),False))
        self.flow.append(0)
        self.c.append(capacity)

    def add_flow(self, edgeInfo,flow):                          # try to add flow at the edge: edgeInfo
        if edgeInfo.foward:                                     # forward
            self.flow[edgeInfo.ind] += flow
        else:                                                   # backward
            self.flow[edgeInfo.ind] -= flow

    def traversable(self,edge):                                 # check if we could send flow on this edge
        return self.left_over_capacity(edge)>0

    def left_over_capacity(self,edge):                          # check if we could send flow on this edge
        if edge.foward:
            return self.c[edge.ind] -self.flow[edge.ind]        # capacity - current flow on this edge
        else:
            return self.flow[edge.ind]                          # current flow on this edge, we could at most send this much back

def bfs(g,n,source,dest):
    edge_taken = [None for _ in range(n)]
    visited = [False for _ in range(n)]

    visited[source]= True
    # queue = deque()
    queue= []
    queue.append(source)
    while queue:
        v= queue.pop(0)
        for edge in g.adj_list[v]:                                      # edges can go from node v
            if g.traversable(edge) and not visited[edge.to]:                # if we could send flow on one edge
                visited[edge.to]=True
                edge_taken[edge.to] = edge
                queue.append(edge.to)
    if visited[dest]:                                           # if we meet the sink
        edge_used=[]                                            # store the edge that we used 
        node=dest                                               # we start from the sink
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
g = FlowGraph(n)
for _ in range(m):
    v,u,c = map(int, input().split())
    v -= 1
    u -= 1
    g.add_edge(v,u,c)

flow = edmond_karp(g,n,0,n-1)
print(flow)