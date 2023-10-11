"""
Truck company: wants to send as many trucks as possible from s to t. Limit of number of trucks on each road.


"""

"""
Network flow:
Graph G=(V,E)
Special vertices s(source) and t(sink).
s has no edges in and t has no edges out.
Every edge (e) has a integer capacity c(e)>=0
Flow:
    capacity constraint: every edge e has a flow 0 <=f(e) <= c(e)
    flow conservation: for all u \neq s, t: flow into u equals flow out of u. so we have:
        \sum_{v:(v,u) \in E} f(v,u) = \sum_{v:(v,u) \in E} f(u,v)
    value of flow f is the sum of flows out of s:
        v(f) = \sum_{v:(s,v) \in E} f(e) = f^{out}(s)
    Maximum flow problem: find s-t flow of maximum value

Ford-Fulkerson Algorithm for maximum flow problem:

The maximum flow problem involves determining the maximum amount of flow tha can be sent from a source vertex to a sink
verte in a directed weighted graph.

The algorithm works by iteratively finding an augmenting path, which is a path from the source to the sink in the residual graph, i.e.,
the graph obtainted by subtracting the curent flow from th capacity of each edge. The algorithm then increases the flow along this path by the
maximum possible amount, which is the minimum capacity of the edges along the path.

residual graph of a flow network is a graph which indicates additional possible flow.
Wvery edge of a residual graph has a value called residual capacity which is equal to original capacity of the edge minus current flow.
Residual capacity is basically the current capacity of the edge.


Time complexity is O(max_flow * E). We run a loop until there is no augmenting path. In the worst case, we may add 1 unit flow in every iteration.
Therefore the time complexity becomes O(max_flow * E)

"""

from collections import defaultdict

# using adjacency matrix representation (2D matrix) to represents a directed graph
class Graph:
    def __init__(self,graph):
        self.graph = graph # residual graph
        self.Row = len(graph)

    
    def BFS(self, s, t, parent):
        visited = [False]*self.Row     # mark all vertices are not visited

        queue = []

        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True
        # print(parent)
        return False

    def FordFulkerson(self, source,sink):
        parent = [-1]*self.Row                      # initial the array
        max_flow = 0

        while self.BFS(source,sink,parent):
            path_flow = float("Inf")                # we need get the minimum flow of this augmenting path
            s = sink
            while(s!= source):
                path_flow = min(path_flow, self.graph[parent[s]][s])        # we use the parent array to get this augmenting path
                s = parent[s]

            max_flow += path_flow
            

            # update the residual capacities of the edges and reverse edges along this augmenting path
            v = sink
            while(v!= source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_flow

if __name__ == '__main__':
    graph = [[0,16,13,0,0,0],[0,0,10,12,0,0],[0,4,0,0,14,0],[0,0,9,0,0,20],[0,0,0,7,0,4],[0,0,0,0,0,0]]
    g = Graph(graph)

    source = 0
    sink = 5

    res =  g.FordFulkerson(source,sink)
    print("results:",res)

