#include<stdio.h>
using namespace std;
#include<bits/stdc++.h>

#define X 7
#define N 2
int lookup[10000];

void initialize(){
    int i;
    for(i=0;i<10000;i++){
        lookup[i]=-1;
    }
}

double calPow(int x, int n ){
    if(lookup[n]!=-1){
        return lookup[n];
    }
    if(n==1){
        return x;
    }
    if(n==0){
        return 1;
    }
    int x1=calPow(x,n/2);
    lookup[n/2]=x1;
    int x2=calPow(x,n-(n/2));
    if(n%2!=0){
        lookup[n-(n/2)]=x2;
    }
    int sol=x1*x2;
    lookup[n]=sol;
    return sol;
}

int main(){
    initialize();
    double ans;
    if(N>=0){
        ans=calPow(X,N);
    }
    else{
        ans=1/calPow(X,-1*N);
    }
    cout<<"The value of "<<X<<"^"<<N<<": "<<ans;
    return 0;
}
