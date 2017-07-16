from collections import defaultdict

class Node:
    def __init__(self,src,dest,wt):
        self.v1=src
        self.v2=dest
        self.wt=wt

class Graph:
    def __init__(self,V):
        self.V=V
        self.vertices=defaultdict(list)

    def addEdge(self,src,dest,wt):
        newNode=[dest,wt]
        self.vertices[src].append(newNode)

    def kruskalMST(self):
        edges=[]
        for i in self.vertices.items():
            for j in i[1]:
                node=Node(i[0],j[0],j[1])
                edges.append(node)
        #sorting edges based on wt
        edges=sorted(edges,key=lambda x:x.wt)
        parent=[-1]*self.V
        v_x=set()
        sol=set()
        for i in range(self.V):
            v_x.add(i)
        while(v_x):
            edge=edges.pop(0)
            if find(edge.v1,parent)==find(edge.v2,parent):
                #ignore edge because cycle is detected
                continue
            else:
                updateParent(find(edge.v1,parent),find(edge.v2,parent),parent)
                sol.add(edge)
                #removing visited vertex
                if edge.v1 in v_x:
                    v_x.remove(edge.v1)
                if edge.v2 in v_x:
                    v_x.remove(edge.v2)

        for i in sol:
            print(i.v1,'-',i.v2,'',i.wt)

def find(v,parent):
    if parent[v]==-1:
        return v
    else:
        return find(parent[v],parent)

def updateParent(v1,v2,parent):
    parent[v1]=v2



if __name__ == '__main__':
    g=Graph(4)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)
    g.kruskalMST()
