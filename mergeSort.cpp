#include<bits/stdc++.h>
using namespace std;

void printArray(int arr[], int size){
    int i;
    for(i=0;i<size;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}

void merge(int arr[], int l, int m, int r){
    int n1=m-l+1;
    int n2=r-m;
    int i,j,k;
    int L[n1],R[n2];
    for(i=0;i<n1;i++){
        L[i]=arr[l+i];
    }
    for(j=0;j<n2;j++){
        R[j]=arr[m+1+j];
    }
    i=0,j=0,k=l;
    while(i<n1 && j<n2){
        if(L[i]<R[j]){
            arr[k++]=L[i++];
        }
        else{
            arr[k++]=R[j++];
        }
    }
    if(i<n1){
        arr[k++]=L[i++];
    }
    if(j<n2){
        arr[k++]=R[j++];
    }
    cout<<"After merging...\n";
    for(i=l;i<=r;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}

void mergeSort(int arr[], int l, int r){
    if(r-l<=0){
        return;
    }
    int m=(l+r)/2;
    mergeSort(arr,l,m);
    mergeSort(arr,m+1,r);
    merge(arr,l,m,r);
}

int main(){
    int arr[]={3,2,1,7,6,4,9};
    int n=sizeof(arr)/sizeof(arr[0]);
    int low=0;
    int high=n-1;
    cout<<"Before Sorting..\n";
    printArray(arr,n);
    mergeSort(arr,low,high);
    cout<<"After Sorting..\n";
    printArray(arr,n);
    return 0;
}
