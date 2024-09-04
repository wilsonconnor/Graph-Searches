class Heap:
    def __init__(self):
        self.arr = [] # Heap list
        self.heapsize = 0
        self.position = []
 
    def minHeapify(self, i):
        smallest = i
        l = 2*i + 1 # inline for LEFT() child
        r = 2*i + 2 # inline for RIGHT() child
 
        if (l < self.heapsize) and (self.arr[l][1] < self.arr[smallest][1]):
            smallest = l # left child is smaller
        if (r < self.heapsize) and (self.arr[r][1] < self.arr[smallest][1]):
            smallest = r # right child is smaller (take priority in this case (if l was also true))
 
        # if current index is not the smallest, do a swap
        if smallest != i:
            self.position[self.arr[smallest][0]] = i
            self.position[self.arr[i][0]] = smallest
 
            # Swap nodes, then begin recursion of minHeapify
            self.swap(smallest, i)
            self.minHeapify(smallest)

    def extractMin(self):
        if self.heapsize == 0: # If empty, return nil
            return None

        min = self.arr[0]
 
        lastNode = self.arr[self.heapsize - 1]
        self.arr[0] = lastNode
 
        # Update position of min node
        self.position[lastNode[0]] = 0
        self.position[min[0]] = self.heapsize - 1
 
        self.heapsize -= 1 # Since the heap minimum was just extracted, the size of the array is reduced, and thus heapsize also
        self.minHeapify(0)
 
        return min # Return the minimum
 
    def decreaseKey(self, v, d):
 
        # Get the index of v in the heap 
        i = self.position[v]
 
        # Get the node and update its distance
        self.arr[i][1] = d
 
        while (i > 0) and (self.arr[i][1] < self.arr[(i - 1) // 2][1]): # // to avoid the Python 3.x auto convert to float 
 
            # Swap this node with its parent
            self.position[self.arr[i][0]] = (i-1)//2 
            self.position[self.arr[(i-1)//2][0]] = i
            self.swap(i, (i - 1)//2 )
 
            # Set i to the parent
            i = (i - 1) // 2
    
    def insert(self, v, d):
        newNode = [v, d]
        return newNode

    # Helper function to swap two values in the heap
    def swap(self, x, y):
        tempNode = self.arr[x]
        self.arr[x] = self.arr[y]
        self.arr[y] = tempNode
