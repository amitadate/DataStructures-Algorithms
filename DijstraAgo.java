//http://www.geeksforgeeks.org/greedy-algorithms-set-6-dijkstras-shortest-path-algorithm/
import java.util.*;
import java.lang.*;
import java.io.*;

class DAlgo{
    static final int V=9;
    
    int minKey(int dist[],Boolean dSet[]){
        int val_min=Integer.MAX_VALUE;
        int index=-1;
        int i;
        for(i=0;i<V;i++){
            if(!dSet[i] && dist[i]<val_min){
                val_min=dist[i];
                index=i;
            }
        }
        return index;
    }
    
    void printSolution(int dist[]){
        System.out.println("Vertex   Distance from Source");
        for (int i = 0; i < V; i++)
            System.out.println(i+" \t\t "+dist[i]);
    }
    
    void Dfind(int graph[][], int start){
        Boolean dSet[]=new Boolean[V];
        int dist[]=new int[V];
        int parent[]=new int[V];
        int i,count;
        for(i=0;i<V;i++){
            dist[i]=Integer.MAX_VALUE;
            dSet[i]=false;
        }
        dist[start]=0;
        parent[start]=-1;
        for(count=0;count<V;count++){
            int u=minKey(dist,dSet);
            dSet[u]=true;
            for(int v=0;v<V;v++){
                if(graph[u][v]!=0 && !dSet[v] && graph[u][v]<(dist[v]-dist[u])){
                    parent[v]=u;
                    dist[v]=dist[u]+graph[u][v];
                }
            }
        }
        printSolution(dist);
    }
    
    public static void main(String args[]){
        int graph[][]=new int[][]{{0, 4, 0, 0, 0, 0, 0, 8, 0},
                                  {4, 0, 8, 0, 0, 0, 0, 11, 0},
                                  {0, 8, 0, 7, 0, 4, 0, 0, 2},
                                  {0, 0, 7, 0, 9, 14, 0, 0, 0},
                                  {0, 0, 0, 9, 0, 10, 0, 0, 0},
                                  {0, 0, 4, 14, 10, 0, 2, 0, 0},
                                  {0, 0, 0, 0, 0, 2, 0, 1, 6},
                                  {8, 11, 0, 0, 0, 0, 1, 0, 7},
                                  {0, 0, 2, 0, 0, 0, 6, 7, 0}
                                 };
        
       DAlgo obj=new DAlgo();
       obj.Dfind(graph,0);
    }
}
