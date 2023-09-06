


class directedGraph:
 
    def __init__(self, vertex, edges):
        self.vertex = vertex 
        self.edges = edges
        self.adjacencyList = [[] for j in range(vertex)]              # adjacencyList for directed graph
        for i in range(len(edges)):
            self.adjacencyList[edges[i][0]].append(edges[i][1])
 
    # Function to add an edge to directed graph
    def addEdge(self, u, v):
        self.adjacencyList[u].append(v)
 
    # Function for BFS
    def BFS(self, s, visited):
        queue = []
 
        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
 
        while queue:
            # Dequeue the first node from this queue and print it
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


    def isCycleUtil(self, v, visited, recStack):
        visited[v] = True               # all visited nodes
        recStack[v] = True              # current path (some nodes we visited but not in current path)

        for i in self.adjacencyList[v]:
            """
            i is one of v's neighbour, if we haven't visited i, then we recursivly call this function to check if there is a cycle;
            if we visited i before, and i already in out path, which means we visited i again. so there is a cycle;
            if we visited i before, and i not in our path. we do nothing in this situation.
            we exclude v in our path, because we couldn't find a cycle in current path, we need go to other's neighbour of i.\
            
            recStack represents our current path.
            """
            if visited[i] == False:
                if self.isCycleUtil(i, visited, recStack) == True:
                    return True
            elif recStack[i] == True:
                return True
        recStack[v] = False
        return False


    def isCycle(self):
        visited = [False]* (self.vertex)
        recStack = [False]* (self.vertex)
        for v in range(self.vertex):
            if visited[v] == False:
                if self.isCycleUtil(v, visited, recStack) == True:
                    return True
        return False
 

if __name__ == '__main__':
 
    vertex = 3 # number of nodes in the graph. Id of these nodes starts at 0
    # edges = [[0,2],[1,2],[2,0],[2,3]] # this is disconnected graph
    # edges = [[0,1],[0,2],[1,2],[2,0],[2,3]] # this is connected graph
    edges = [[0,1],[0,2],[1,2],[2,0],[2,3]]                         # this is for checking cycle

    g = directedGraph(vertex, edges) #construct an undirected graph
    
    # g.BFShelper()   # for BFS traverse
    # g.DFS()         # for DFS traverse


    # for checking if there is a cycle in this graph.
    if g.isCycle() == True:
        print("Contains a graph")
    else:
        print("Doesn't contain a graph")
