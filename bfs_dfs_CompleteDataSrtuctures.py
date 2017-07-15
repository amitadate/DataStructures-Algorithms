import queue

class Vertex:
    def __init__(self,data):
        self.data=data
        self.next=None

class Llist:
    def __init__(self):
        self.root=None

    def addVertex(self,b):
        if self.root==None:
            self.root=Vertex(b)
            return
        temp=self.root
        while(temp.next):
            temp=temp.next
        temp.next=Vertex(b)

    def printVertex(self,i):
        temp=self.root
        print(i,'->',end='')
        while(temp):
            print(temp.data,end='')
            temp=temp.next
            if(temp):
                print('->',end='')
        print()

    def addAllVertexToQ(self,q,visited):
        temp=self.root
        while(temp):
            if temp.data not in visited:
                q.put(temp.data)
                visited.add(temp.data)
            temp=temp.next

    def addAllVertexToS(self,st,visited):
        temp=self.root
        while(temp):
            if temp.data not in visited:
                st.append(temp.data)
                visited.add(temp.data)
            temp=temp.next



class Graph:
    def __init__(self,V):
        self.V=V
        self.vertices=[Llist() for i in range(V)]

    def addEdge(self, a, b):
        self.vertices[a].addVertex(b)

    def printGraph(self):
        for i in range(self.V):
            self.vertices[i].printVertex(i)

    def addNeighbourQ(self,q,item,visited):
        self.vertices[item].addAllVertexToQ(q,visited)

    def addNeighbourS(self,st,item,visited):
        self.vertices[item].addAllVertexToS(st,visited)

    def bfs(self,start):
        q=queue.Queue()
        q.put(start)
        visited=set()
        visited.add(start)
        while(not q.empty()):
            item=q.get()
            print(item,' ',end='')
            self.addNeighbourQ(q,item,visited)
        print()

    def dfs(self,start):
        st=[]
        st.append(start)
        visited=set()
        visited.add(start)
        while(len(st)!=0):
            item=st.pop()
            print(item,' ',end='')
            self.addNeighbourS(st,item,visited)
        print()



if __name__ == '__main__':
    g=Graph(4)
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 0);
    g.addEdge(2, 3);
    g.addEdge(3, 3);
    g.printGraph()
    g.bfs(2)
    g.dfs(2)
