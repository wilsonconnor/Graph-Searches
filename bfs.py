# Class to use for BFS (Unweighted graphs)
class GraphUW:
    def __init__(self, nodeAmt):
        self.numNodes = nodeAmt
        self.nodes = range(self.numNodes)
        self.adjList = {node: set() for node in cityList} 

    def addVertex(self, vertexList): # Add vertices into the adj list
        for i in range(len(vertexList)):
            self.adjList[i] = vertexList[i]

    def addEdge(self, node1, node2): # Add edges into the adj list
        self.adjList[node1].add(node2)
        self.adjList[node2].add(node1)

    def bfs(self, s, t): # Let s be the root node, or startpoint, and t be the target node, or endpoint. 
        gray = [] # Instead of using a node object, a list is made where the node is added once searched 
        Q = [[s]] # Create and initialize queue using the root node
        while Q:
            u = Q.pop(0) # Remove first element in the queue, rather than the last element
            node = u[-1]

            if node not in gray:
                v = self.adjList[node]

                for adj in v:
                    path = list(u) # Think of this as a predecessor list
                    path.append(adj)
                    Q.append(path)

                    if adj == t: # If target node is reached
                        return path # Return shortest path once found

                gray.append(node)
