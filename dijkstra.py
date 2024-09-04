# Class to use for Dijkstra (Weighted graph)
class GraphW:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list) # The use of defaultdict instead of dict is so that a key error is not thrown when accessing index(0) --> this ensures 0 is present
 
    # Adds an undirected edge to the graph
    def addEdge(self, node1, node2, weight):

        tempNode1 = [node2, weight]
        tempNode2 = [node1, weight]

        self.graph[node1].insert(0, tempNode1)
        self.graph[node2].insert(0, tempNode2)
 
    def dijkstra(self, s, t): # s = start node, t = target (passed into print array)
        V = self.V  # Num of vertices in graph
        d = []   # Distance value list
        path = defaultdict(list) # Predecessor list
 
        heap = Heap()
 
        # Inline version of singleSource() from text
        for v in range(V):
            d.append(math.inf)
            heap.arr.append(heap.insert(v, d[v]))
            heap.position.append(v)
 
        heap.position[s] = s
        d[s] = 0
        heap.decreaseKey(s, d[s])
 
        # Initial size of min heap is equal to amt of vertices
        heap.heapsize = V
 
        while heap.heapsize != 0: 
            node = heap.extractMin()
            u = node[0]
 
            for i in self.graph[u]:
                v = i[0]
                # If shortest distance to v isn't final and dist. to v through u is less, then it's prev. distance
                if (heap.position[v] < heap.heapsize) and (d[u] != math.inf) and (i[1] + d[u] < d[v]):
                        d[v] = i[1] + d[u] # Inline relax() from text
                        path[v].insert(0, u)
                        heap.decreaseKey(v, d[v])
                        
 
        printPath(d, V, path, s, t)

def printPath(d, v, path, s, t):
    fullPath = []
    pathDone = False
    fullPath.append(cityList[t])
    cost = d[t]
    while pathDone is False:
        fullPath.append(cityList[path[t][0]])
        t = path[t][0]
        if t == 0:
            pathDone = True

    fullPath.reverse()
    print("Shortest path from Arad to Bucharest -> ", fullPath, 'with total cost of', cost)
