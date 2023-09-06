"""
A Graph is composed of a set of vertices( V ) and a set of edges( E ). The graph is denoted by G(E, V).

We could use adjacency matrix and adjacency list to represent a graph.
creating a graph with vertices and edges;

displaying a graph;

traversals in graphs: Depth first search traversal, Breadth First Search Traversal


"""
 
class undirectedGraph:
 
    def __init__(self, vertex, edges):
        self.vertex = vertex 
        self.edges = edges

        self.adjacencyList = [[] for j in range(vertex)]              # adjacencyList for undirected graph
        for i in range(len(edges)):
            self.adjacencyList[edges[i][0]].append(edges[i][1])
            self.adjacencyList[edges[i][1]].append(edges[i][0])
 
    # Function to add an edge to undirected graph
    def addEdge(self, u, v):
        self.adjacencyList[u].append(v)
        self.adjacencyList[v].append(u)
 
    # Function for BFS
    def BFS(self, s, visited):
        queue = []
 
        queue.append(s)
        visited[s] = True
 
        while queue:
            v = queue.pop(0)
            print(v, end=" ")
 
            # Get all adjacent vertices of the dequeued vertex s.
            # If an adjacent has not been visited, then mark it visited and enqueue it
            for i in self.adjacencyList[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
    
    def BFShelper(self):                # help for disconnected graph
        if self.vertex == 0:
            return
        visited = [False] * self.vertex
        for i in range(self.vertex):
            if visited[i] == False:
                self.BFS(i, visited)

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=" ")
        for i in self.adjacencyList[v]:
            if i not in visited:
                self.DFSUtil(i, visited)

    def DFS(self):
        if self.vertex == 0:
            return
        visited = set()

        for v in range(self.vertex):
            if v not in visited:
                self.DFSUtil(v, visited)
    

    def isCycleUtil(self, v, visited, parent):
        visited[v] = True
        """
        i is one of v's neighbor. 
        if we haven't visite i, then we recursively call this function (run DFS) on this node to check if there is a cycle.
        if we visited node i before, and node i is not the parent node, which mean there are two i in our current path, so there is a cycle;
        if we visited node i before, and node i is the parent node. we do nothing in this situation. Because this is a undirected graph, 
        node i is actually just the previous node v.
        """
        for i in self.adjacencyList[v]:
            if visited[i] == False:
                if self.isCycleUtil(i, visited, v) == True:
                    return True
            elif i != parent:
                return True
        return False


    def isCycle(self):
        visited = [False]* (self.vertex)
        for v in range(self.vertex):
            if visited[v] == False:
                if self.isCycleUtil(v, visited, v) == True:
                    return True
        return False
 

if __name__ == '__main__':
 
    vertex = 4                                      # number of nodes in the graph. Id of these nodes starts at 0
    # edges = [[0,2],[1,2],[2,0],[2,3]]               # this is disconnected graph
    # edges = [[0,1],[0,2],[1,2],[2,0],[2,3]]       # this is connected graph
    # edges = [[1,0],[1,2],[2,0],[0,3],[3,4]]                         # this is a cycle
    edges = [[0,1],[1,2],[2,3]]                                       # no cycle in this graph

    g = undirectedGraph(vertex, edges)              # construct an undirected graph
    
    # g.BFShelper()    # for BFS traverse
    # g.DFS()            # for DFS traverse

    # for checking if there is a cycle in this graph.
    if g.isCycle() == True:
        print("Contains a graph")
    else:
        print("Doesn't contain a graph")