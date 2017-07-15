from collections import defaultdict
import sys

class Graph:
    def __init__(self,V):
        self.V=V
        self.vertices=defaultdict(list)

    def addEdge(self,src,dest,wt):
        newNode=[dest,wt]
        self.vertices[src].append(newNode)
        newNode=[src,wt]
        self.vertices[dest].append(newNode)

    def printGraph(self):
        for i in range(self.V):
            print(i,'->',self.vertices[i])

    def primMST(self):
        dist=[sys.maxsize]*self.V
        parent=[None]*self.V
        x=set()
        v_x=set()
        for i in range(self.V):
            v_x.add(i)
        #adding the source vertex
        x.add(0)
        v_x.remove(0)
        dist[0]=0
        for k,v in self.vertices[0]:
            dist[k]=v
            parent[k]=0
        while(v_x):
            min=sys.maxsize
            min_vertex=None
            #choosing next vertex according to greedy criterion
            for i in v_x:
                if dist[i]<min:
                    min=dist[i]
                    min_vertex=i
            #add min_vertex to set x
            x.add(min_vertex)
            v_x.remove(min_vertex)
            #update the dist of neighbouring vertex to min_vertex
            for k,v in self.vertices[min_vertex]:
                if dist[k]>v and k in v_x:
                    dist[k]=v
                    parent[k]=min_vertex
        #print MST
        print('The MST is')
        for i in range(1,self.V):
            print(parent[i],'->',i)


if __name__ == '__main__':
    graph=Graph(9)
    graph.addEdge(0, 1, 4)
    graph.addEdge(0, 7, 8)
    graph.addEdge(1, 2, 8)
    graph.addEdge(1, 7, 11)
    graph.addEdge(2, 3, 7)
    graph.addEdge(2, 8, 2)
    graph.addEdge(2, 5, 4)
    graph.addEdge(3, 4, 9)
    graph.addEdge(3, 5, 14)
    graph.addEdge(4, 5, 10)
    graph.addEdge(5, 6, 2)
    graph.addEdge(6, 7, 1)
    graph.addEdge(6, 8, 6)
    graph.addEdge(7, 8, 7)
    graph.printGraph()
    graph.primMST()
