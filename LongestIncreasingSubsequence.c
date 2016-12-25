#include<stdio.h>
#include<stdlib.h>
#define MAX 100
int lookup[MAX];
int check[MAX];
void initialize(int n){
    int i;
    for(i=0;i<n;i++){
        lookup[i]=1;
        check[i]=0;
    }
}

int _lis(int arr[], int n, int *max_list){
    if(n==1){
        return 1;
    }
    int current_list=1;
    int i;
    for(i=0;i<n-1;i++){
        int present_val;
        if(check[i]==1){
            present_val=lookup[i];
        }
        else{
            present_val=_lis(arr,i,max_list);
        }
        
        if(arr[i]<arr[n-1]&&current_list<1+present_val){
            current_list=1+present_val;
        }
    }
    if(*max_list<current_list){
        *max_list=current_list;
    }
    check[n]=1;
    lookup[n]=current_list;
    return current_list;
}

int lis(int arr[],int n){
    int max_list=1;
    int x=_lis(arr,n,&max_list);
    return max_list;
}

int main(){
    int arr[] = {3, 2};
    int n = sizeof(arr)/sizeof(arr[0]);
    initialize(n);
    printf("Length of LIS is %d\n", lis( arr, n ));
    return 0;
}
