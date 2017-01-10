//http://www.geeksforgeeks.org/find-the-minimum-cost-to-reach-a-destination-where-every-station-is-connected-in-one-direction/
#include<stdio.h>
using namespace std;
#include<bits/stdc++.h>
#include<limits.h>
#define N 4
#define INF INT_MAX
int lookup[N][N];

//initializing lookup table with minimum cost(between 2 stations)=infinity
void initialize(){
    int i,j;
    for(i=0;i<N;i++){
        for(j=0;j<N;j++){
            lookup[i][j]=-1;
        }
    }
}

int minCost(int i, int j, int cost[N][N]){
    if(lookup[i][j]!=-1){
        return lookup[i][j];
    }
    if(j-i==1){
        return cost[i][j];
    }
    int min=INF;
    int n,dist;
    for(n=i+1;n<j;n++){
        int optimize=minCost(n,j,cost);
        lookup[n][j]=optimize;
        dist=cost[i][n]+optimize;
        if(dist<min){
            min=dist;
        }
    }
    if(min<cost[i][j]){
        lookup[i][j]=min;
        return min;
    }
    else{
        lookup[i][j]=cost[i][j];
        return cost[i][j];
    }
    
}

int main(){
    initialize();
    int cost[N][N]={ {0, 15, 80, 90},
                      {INF, 0, 40, 50},
                      {INF, INF, 0, 5},
                      {INF, INF, INF, 0}
                    };
    int ans=minCost(0,N-1,cost);
    cout<<"The minimum cost to reach "<<N<<" is "<<ans;
    return 0;
}
