
# we use edmond_karp algorithm to solve this problem

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

    def traversable(self,edge):
        return self.left_over_capacity(edge) > 0
        

    def left_over_capacity(self,edge):
        if edge.forward:
            return self.c[edge.ind]- self.flow[edge.ind]
        else:
            return self.flow[edge.ind]
    

def bfs(g,n,source,sink):
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
    if visited[sink]:
        edge_used = []
        node = sink
        while edge_taken[node]:
            edge_used.append(edge_taken[node])
            node = edge_taken[node].frm
        return edge_used
    return None



"""
In edmond_karp algorithm, every time, we pick up the shortest path using BFS, and send as much flow as we can.
"""
def edmond_karp(g,n,source,sink):
    while True:
        path = bfs(g,n,source,sink)
        if path is None:
            break
        flow = g.left_over_capacity(path[0])
        for edge in path:
            flow = min(flow,g.left_over_capacity(edge))
        for edge in path:
            g.add_flow(edge,flow)
    
    totoal_flow = 0
    for edge in g.adj_list[source]:
        if edge.forward:
            totoal_flow += g.flow[edge.ind]
    
    return totoal_flow

n,m = map(int,input().split())

g=DSGraph(n)
for _ in range(m):
    frm,to,c = map(int,input().split())
    frm-=1
    to-=1
    g.add_edge(frm,to,c)
print(edmond_karp(g,n,0,n-1))


