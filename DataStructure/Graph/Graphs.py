"""
A Graph is composed of a set of vertices( V ) and a set of edges( E ). The graph is denoted by G(E, V).

We could use adjacency matrix and adjacency list to represent a graph.
creating a graph with vertices and edges;

displaying a graph;

traversals in graphs: Depth first search traversal, Breadth First Search Traversal


"""

from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False] * (max(self.graph) + 1)
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:
            v = queue.pop(0)
            print("node:", v)

            for i in self.graph[v]:
                if visited[i] == False:
                    queue.append(v)
                    visited[i] == True

if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
 
    print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
    g.BFS(2)
