#include<bits/stdc++.h>
using namespace std;
#define N 10

void printSolution(int arr[N][N])
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
            cout<<arr[i][j]<<" ";
        cout<<endl;
    }
}

bool isSafe(int arr[N][N],int row, int col){
    int i,j;
    //check left side of the row
    for(i=0;i<col;i++){
        if(arr[row][i]){
            return false;
        }
    }
    //check left side of the upper diagonal
    for(i=row-1,j=col-1;i>=0 && j>=0;j--,i--){
            if(arr[i][j]){
                return false;
        }
    }
    //check left side of the lower diagonal
    for(i=row+1,j=col-1;i<N && j>=0;j--,i++){
            if(arr[i][j]){
                return false;
        }
    }
    return true;
}

bool NQ(int arr[N][N],int col){
    if(col>=N){
        return true;
    }
    
    int row;
    for(row=0;row<N;row++){
        if(isSafe(arr,row,col)){
            //Placing the queen on the square 
            arr[row][col]=1;
            
            //trying to find solution with the above placement
            if(NQ(arr,col+1)){
                //if NQ returns true that means solution found hence return true
                return true;
            }
            //else backtrack
            arr[row][col]=0;
        }
    }
    
    if(row==N){
        return false;
    }
}

void NQUtil(){
    int arr[N][N]={{0,0,0,0},
                    {0,0,0,0},
                    {0,0,0,0},
                    {0,0,0,0}};
    int col=0;
    bool sol=NQ(arr,col);
    if(sol){
        cout<<"Found Solution with config :\n";
        printSolution(arr);
    }
    else{
        cout<<"Oops!\n";
    }
}

int main(){
    NQUtil();
    return 0;
}
