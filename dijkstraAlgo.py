#http://www.geeksforgeeks.org/greedy-algorithms-set-6-dijkstras-shortest-path-algorithm/

from sys import maxsize

class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.graph=[[0 for columns in range(vertices)]for rows in range(vertices)]

    def dijkstra(self,start):
        a=[maxsize]*self.vertices
        #initializing a[start]
        a[start]=0
        x=set()
        v_x=set()
        for i in range(self.vertices):
            v_x.add(i)
        x.add(start)
        v_x.remove(start)
        while(v_x):
            min_dist=maxsize
            add_node=None
            for x_node in x:
                for v_node in v_x:
                    if a[x_node]+self.graph[x_node][v_node]<min_dist and self.graph[x_node][v_node]!=0 :
                        min_dist=a[x_node]+self.graph[x_node][v_node]
                        add_node=v_node
            #add node from v_x to x
            x.add(add_node)
            v_x.remove(add_node)
            a[add_node]=min_dist
        return a





g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ];

a=g.dijkstra(0)
for i in range(len(a)):
    print(i,'->',a[i])
