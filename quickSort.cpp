#include<bits/stdc++.h>
using namespace std;


void printArray(int arr[], int size)
{
    //int size=sizeof(arr)/sizeof(arr[0]);
    int i;
    for (i=0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}


void swap(int arr[],int i,int j){
    int temp;
    temp=arr[i];
    arr[i]=arr[j];
    arr[j]=temp;
}

int partition(int arr[], int low, int high){
    int i=low-1;
    int j;
    int pivot=arr[high];
    for(j=low;j<high;j++){
        if(arr[j]<=pivot){
            i++;
            swap(arr,i,j);
        }
    }
    swap(arr,i+1,high);
    return (i+1);
}

void quickSort(int arr[], int low, int high){
    
    if(high-low<0)
        return;
    printf("Before partition...\n");
    printArray(arr,7);
    int pi=partition(arr,low,high);
    printf("After partition...\n");
    printArray(arr,7);
    quickSort(arr,low,pi-1);
    quickSort(arr,pi+1,high);
}


int main(){
    int arr[]={3,2,4,8,6,1,5};
    int low=0;
    int n=sizeof(arr)/sizeof(arr[0]);
    printf("Before Sorting...\n");
    printArray(arr,n);
    int high=n-1;
    quickSort(arr,low,high);
    printf("After Sorting...\n");
    printArray(arr,n);
    return 0;
}
