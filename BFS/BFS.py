# -*- coding: utf-8 -*-

#Breadth-First Search algorithm

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
                
    def BFS(self):         
        visited=[]
        queue = []        
        
        for i in self.vertices:
            if i not in visited:
                visited.append(i)
                queue.append(i)             
                while queue:
                    s = queue.pop(0) 
                    print (s, end = " ")                     
                    for neighbour in self.graph[s]:
                        if neighbour not in visited:
                            visited.append(neighbour)
                            queue.append(neighbour)
                     
g = Graph() 
g.addEdge(0, 1)
g.addEdge(0, 2) 
g.addEdge(1, 3) 
g.addEdge(2, 4) 
g.addEdge(2, 3) 
g.addEdge(5, 6) 
g.BFS()
