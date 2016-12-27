#include <iostream>
#include<string.h>
using namespace std;


int lcs(char *X, char *Y, int m, int n){
    if(m==0 || n==0){
        return 0;
    }
    if(X[m-1]==Y[n-1]){
        return 1+lcs(X,Y,m-1,n-1);
    }
    else{
        return max(lcs(X,Y,m-1,n),lcs(X,Y,m,n-1));
    }
}

int max(int a, int b){
    return (a>b)?a:b;
}

int main(){
    
    char X[] = "ABCDGH";
    char Y[] = "AEDFHR";
     
    int m = strlen(X);
    int n = strlen(Y);
     
    printf("Length of LCS is %d\n", lcs( X, Y, m, n ) );
     
    return 0;
}
