#include<stdio.h>
#include<bits/stdc++.h>
using namespace std;

int lookup[10000][10000];

int min(int x, int y, int z){
    return min(min(x,y),z);
}


int minEdit(string str1, string str2, int m, int n, int lookup[10000][10000]){
    if(m==0){
        return n;
    }
    if(n==0){
        return m;
    }
    if(lookup[m-1][n-1]!=-1){
        return lookup[m-1][n-1];
    }
    if(str1[m-1]==str2[n-1]){
        lookup[m-1][m-1]= minEdit(str1,str2,m-1,n-1,lookup);
        return lookup[m-1][m-1];
    }
    lookup[m-1][n-1]= 1+min(minEdit(str1,str2,m-1,n-1,lookup),
    minEdit(str1,str2,m-1,n,lookup),minEdit(str1,str2,m,n-1,lookup));
    return lookup[m-1][n-1];

}

void initialize(int lookup[10000][10000], int m, int n){
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            lookup[i][j]=-1;
        }
    }
}

int main(){
    string str1 = "cut";
    string str2 = "cat";
    initialize(lookup,str1.length(),str2.length());
    cout << minEdit( str1 , str2 , str1.length(), str2.length(),lookup);
 
    return 0;
}
