#include<stdio.h>
#define R 3
#define C 3
int lookup[R][C];

void initialize(){
    for(int i=0;i<R;i++){
        for(int j=0;j<C;j++){
            lookup[i][j]=-1;
        }
    }
}

int min(int x, int y, int z)
{
if (x < y)
	return (x < z)? x : z;
else
	return (y < z)? y : z;
}

int minCost(int cost[R][C],int m, int n){
    if(lookup[m][n]!=-1){
        return lookup[m][n];
    }
    if(m==0 && n==0){
        lookup[m][n]=cost[m][n];
        return cost[m][n];
    }
    if(m==0){
        int sum=0;
        for(int i=0; i<=n;i++){
            sum+=cost[m][i];
        }
        lookup[m][n]=sum;
        return sum;
    }
    if(n==0){
        int sum=0;
        for(int i=0; i<=n;i++){
            sum+=cost[i][n];
        }
        lookup[m][n]=sum;
        return sum;
    }
    lookup[m][n]=cost[m][n]+min(minCost(cost,m-1,n-1),minCost(cost,m,n-1),minCost(cost,m-1,n));
    return lookup[m][n];
}

int main(){
    
    int cost[R][C] = { {1, 2, 3},
                      {4, 8, 2},
                      {1, 5, 3} };
    initialize();
    printf(" %d ", minCost(cost, 2, 2));
    return 0;
}
