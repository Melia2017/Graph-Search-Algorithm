# -*- coding: utf-8 -*-

from collections import defaultdict 
  
class Graph: 
  
    def __init__(self): 
        self.graph = defaultdict(list) 
        self.num=0
        self.vertices=[]
  
    # function to add an edge to graph 
    def addEdge(self, u, v): 
        self.graph[u].append(v)
        #calculate the number of vertices
        for i in [u,v]:
            if i not in self.vertices:
                self.vertices.append(i)
                self.num+=1
                
    # A recursive function that will be utilized by DFSTraversal
    def DFS(self, v, visited): 
  
        # Mark the current vertex as visited and print it 
        visited[v] = True
        print(v, end = ' ') 
  
        # Repeat for all the adjacent vertices
        for i in self.graph[v]: 
            if i not in self.graph:
                visited[i] = True
                print(i,end=' ')
            else:
                if visited[i] == False: 
                    self.DFS(i, visited) 
   
    def DFSTraversal(self):
        # Mark all the vertices as not visited 
        visited = [False] * self.num
  
        # Call the recursive function for all vertices        
        for i in self.graph:
            if visited[i]==False:
                self.DFS(i, visited) 
                
# Create a graph
g = Graph() 
g.addEdge(0, 1)
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(4, 5) 
g.addEdge(4, 6) 

print(g.graph)
print("Following is DFS from (starting from vertex 2)") 
g.DFSTraversal() 




