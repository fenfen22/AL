"""
flow network: is a directed graph in which each edge has a capacity or the most flow that can possibly pass through it

Residual graph: The capacity of the edges in the residual graph is updated in accordance with the current flow,
making it a modified version of the original flow network. 
It represents the amount of additional flow that each edge can still handle.

Augmenting path: In the residual graph, an augmenting path is one that connects the source and sink while having 
positive edge capacities. The network's flow increases by using augmenting paths.

In Dinic, we use BFS to check f mre flow is possible and to construct level graph. 
In level graph, we assign levels to all nodes, level of a node is shortest distance (in term of number os edges) of the 
node from the source. Once level graph is constructed, we send multiple flows ysng this level graph.
"""

class Edge:
    def __init__(self, v, flow,C,rev):
        self.v = v                          # the node pointed by this edge
        self.flow = flow                    # current flow of this edge
        self.C = C                          # capacity of this edge
        self.rev = rev                      # array stored other edges that we could go
class Graph:
    def __init__(self, v):
        self.adj = [[] for i in range(v)]    # adjancy array
        self.v = v
        self.level = [0 for i in range(v)]

    def addEdge(self,u,v,C):

        foredg = Edge(v,0,C,len(self.adj[v]))               # forward edge: points to node v, with 0 current flow and C capacity, number of edges can go from node v
        bacedg = Edge(u,0,0,len(self.adj[u]))               # backard edge: points to node u, with 0 current flow and 0 capacity, number of edges can go from node u

        self.adj[u].append(foredg)                          # from u, we could go to v
        self.adj[v].append(bacedg)
    
    def BFS(self,source,sink):
        for i in range(self.v):
            self.level[i] = -1                              # initial the level array, level array works as visited array
        
        self.level[source] = 0

        q = []
        q.append(source)

        while q:
            u = q.pop(0)
            for i in range(len(self.adj[u])):               #self.adj[u] contains all nodes that can go from node u
                e = self.adj[u][i]
                if self.level[e.v] < 0 and e.flow < e.C:    # if the level of this node haven't been set, and flow < C, then set its level
                    self.level[e.v] = self.level[u] + 1
                    q.append(e.v)
        
        return False if self.level[sink] < 0 else True      # if we could not find a way from source to sink, then return false

    def sendFlow(self, u, flow, t, start):                  # start[]: to keep track of next edge to be explored. for example: start[i] stores number of edge to be explored from i
        if u == t:
            return flow
        while start[u] < len(self.adj[u]):
            e = self.adj[u][start[u]]
            if self.level[e.v] == self.level[u]+1 and e.flow < e.C:
                cur_flow = min(flow, e.C-e.flow)
                temp_flow = self.sendFlow(e.v, cur_flow, t, start)

                if temp_flow and temp_flow > 0:

                    e.flow += temp_flow
                    self.adj[e.v][e.rev].flow -= temp_flow              # subtract flow for reverse edge of current edge
                    return temp_flow
            start[u] += 1
    
    def DinicMaxFlow(self,s,t):
        if s == t:
            return -1
        total = 0

        while self.BFS(s,t) == True:
            start = [0 for i in range(self.v+1)]
            while True:
                flow = self.sendFlow(s, float('inf'), t, start)
                if not flow:
                    break
                total += flow
        return total
        


if __name__ == '__main__':
    g=Graph(6)
    # List = [[0,1,16],[0,2,13],[1,2,10],[1,3,12],[2,1,4],[2,4,14],[3,2,9],[3,5,20],[4,3,7],[4,5,4]]

    g.addEdge(0,1,16)
    g.addEdge(0,2,13)
    g.addEdge(1,2,10)
    g.addEdge(1,3,12)
    g.addEdge(2,1,4)
    g.addEdge(2,4,14)
    g.addEdge(3,2,9)
    g.addEdge(3,5,20)
    g.addEdge(4,3,7)
    g.addEdge(4,5,4)

    res = g.DinicMaxFlow(0,5)
    print(res)
    # print(g.adj)
    level = [0 for i in range(6)]
    print(level)
    