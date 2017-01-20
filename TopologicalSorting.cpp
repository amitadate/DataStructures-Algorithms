//http://www.geeksforgeeks.org/topological-sorting/
#include<bits/stdc++.h>
using namespace std;
#include<list>
#include<stack>

class Graph{
    int V;
    list<int> *adj;
    public:
    void addEdge(int v, int w);
    void topSortUtil(int v,bool visited[], stack<int> &Stack);
    void topSort();
    Graph(int v);
};

Graph::Graph(int v){
    V=v;
    adj=new list<int>[V];
}

void Graph::addEdge(int v, int w){
    adj[v].push_back(w);
}

void Graph::topSortUtil(int v,bool visited[], stack<int> &Stack){
    visited[v]=true;
    list<int>::iterator ii;
    for(ii=adj[v].begin();ii!=adj[v].end();++ii){
        if(!visited[*ii]){
            topSortUtil(*ii,visited,Stack);
        }
    }
    Stack.push(v);
}

void Graph::topSort(){
    bool visited[V];
    stack<int> Stack;
    int i;
    for(i=0;i<V;i++){
        visited[i]=false;
    }
    
    for(i=0;i<V;i++){
        if(!visited[i]){
            topSortUtil(i,visited,Stack);
        }
    }
    
    while(!Stack.empty()){
        cout<<Stack.top()<<" ";
        Stack.pop();
    }
}

int main(){
    Graph g(6);
    g.addEdge(5, 2);
    g.addEdge(5, 0);
    g.addEdge(4, 0);
    g.addEdge(4, 1);
    g.addEdge(2, 3);
    g.addEdge(3, 1);
 
    cout << "Following is a Topological Sort of the given graph \n";
    g.topSort();
 
    return 0;
}
