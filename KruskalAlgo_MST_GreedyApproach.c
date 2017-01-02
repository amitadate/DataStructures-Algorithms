#include <iostream>
using namespace std;


struct Edge{
    int src,dest,weight;
};

struct Graph{
    int V,E;
    struct Edge* edge;
};

struct Graph* createGraph(int V,int E){
    struct Graph* graph=(struct Graph*)malloc(sizeof(struct Graph));
    graph->V=V;
    graph->E=E;
    graph->edge=(struct Edge*)malloc(graph->E*sizeof(struct Edge));
}

int myComp(const void* a, const void* b){
    struct Edge* a1=(struct Edge*)a;
    struct Edge* b1=(struct Edge*)b;
    return a1->weight>b1->weight;
}

void KruskalMST(struct Graph* graph){
    int V=graph->V;
    struct Edge result[V];
    int e=0;
    int i=0;
    int check[V];
    for(i=0;i<V;i++){
        check[i]=0;
    }
    qsort(graph->edge,graph->E,sizeof(graph->edge[0]),myComp);
    i=0;
    int src=graph->edge[i].src;
    int dest=graph->edge[i].dest;
    result[e++]=graph->edge[i++];
    check[src]=1;
    check[dest]=1;
    while(e<V-1){
        int src=graph->edge[i].src;
        int dest=graph->edge[i].dest;
        struct Edge nextEdge=graph->edge[i++];
        if(!(check[src]==1 && check[dest]==1)){
            result[e++]=nextEdge;
            check[src]=1;
            check[dest]=1;
        }
    }
    printf("\nFollowing are the edges in the MST\n");
    for(i=0;i<e;i++){
        printf("%d -- %d == %d\n", result[i].src, result[i].dest,result[i].weight);
    }
    return;
}

int main() {
	int v=4;
	int e=5;
	struct Graph* graph=createGraph(v,e);
	
	// add edge 0-1
	graph->edge[0].src = 0;
    graph->edge[0].dest = 1;
    graph->edge[0].weight = 10;
 
    // add edge 0-2
    graph->edge[1].src = 0;
    graph->edge[1].dest = 2;
    graph->edge[1].weight = 6;
 
    // add edge 0-3
    graph->edge[2].src = 0;
    graph->edge[2].dest = 3;
    graph->edge[2].weight = 5;
 
    // add edge 1-3
    graph->edge[3].src = 1;
    graph->edge[3].dest = 3;
    graph->edge[3].weight = 15;
 
    // add edge 2-3
    graph->edge[4].src = 2;
    graph->edge[4].dest = 3;
    graph->edge[4].weight = 4;
    
    KruskalMST(graph);
 
	return 0;
}
