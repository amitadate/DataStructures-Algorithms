#include<stdio.h>
using namespace std;
#include<bits/stdc++.h>

void swap(char *a,char *b){
    char temp;
    temp=*a;
    *a=*b;
    *b=temp;
}

void permutation(char *ch,int l,int r){
    if(l==r){
        cout<<ch<<"\n";
    }
    else{
    int i;
    for(i=l;i<=r;i++){
        swap(ch+l,ch+i);
        permutation(ch,l+1,r);
        swap(ch+l,ch+i);//backtrack step
    }
    }
}


int main(){
    char ch[]="ABC";
    int len=strlen(ch);
    permutation(ch,0,len-1);
    return 0;
}
