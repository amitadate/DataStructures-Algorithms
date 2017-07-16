from collections import defaultdict

class Graph:
    def __init__(self,V):
        self.V=V
        self.vertices=defaultdict(list)

    def addEdge(self,src,dest):
        self.vertices[src].append(dest)

    def topSort(self):
        visited=set()
        st=[]
        for i in range(self.V):
            if i not in visited:
                self.dfs(i,st,visited)

        while(len(st)!=0):
            print(st.pop(),' ',end='')

    def dfs(self,i,st,visited):
        visited.add(i)
        nbour=[]
        for j in self.vertices[i]:
            if j not in visited:
                nbour.append(j)

        while(len(nbour)!=0):
            self.dfs(nbour.pop(),st,visited)

        st.append(i)

if __name__ == '__main__':
    g= Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    g.topSort()
