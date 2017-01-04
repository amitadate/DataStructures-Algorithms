#include<stdio.h>
using namespace std;
#include<limits.h>
#include<bits/stdc++.h>
#define V 5

int findMinKey(int key[V], bool mstSet[V]){
    int min=INT_MAX;
    int index;
    int i;
    for(i=0;i<V;i++){
        if(mstSet[i]==false && key[i]<min){
            min=key[i];
            index=i;
        }
    }
    return index;
}

void printMst(int parent[V], int graph[V][V]){
    int i;
    for(i=1;i<V;i++){
        cout<<parent[i]<<"->"<<i<<" "<<graph[i][parent[i]]<<"\n";
    }
}

void primMst(int graph[V][V]){
    int key[V];
    int parent[V];
    bool mstSet[V];
    int i;
    for(i=0;i<V;i++){
        key[i]=INT_MAX;
        mstSet[i]=false;
    }
    key[0]=0;
    parent[0]=-1;
    int count=0;
    while(count<V){
        int u=findMinKey(key,mstSet);
        count++;
        mstSet[u]=true;
        int v;
        for(v=0;v<V;v++){
            if(graph[u][v] && mstSet[v]==false && (graph[u][v]<key[v])){
                key[v]=graph[u][v];
                parent[v]=u;
            }
        }
    }
    printMst(parent,graph);
}

int main(){
    int graph[V][V]={{0, 2, 0, 6, 0},
                      {2, 0, 3, 8, 5},
                      {0, 3, 0, 0, 7},
                      {6, 8, 0, 0, 9},
                      {0, 5, 7, 9, 0},
                     };
                     
    primMst(graph);
    return 0;
}
