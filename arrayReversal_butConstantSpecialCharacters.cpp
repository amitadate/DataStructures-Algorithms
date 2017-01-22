//http://www.geeksforgeeks.org/reverse-an-array-without-affecting-special-characters/
#include<bits/stdc++.h>
#include<ctype.h>
using namespace std;

void swap(char rev[],char ch[], int i,int j){
    rev[i]=ch[j];
    rev[j]=ch[i];
}

int main(){
    char ch[]="Ab,c,de!$";
    cout<<"Initial array: "<<ch<<endl;
    int l=sizeof(ch)/sizeof(ch[0]);
    char rev[l];
    int j=l-1;
    int i=0;
    while(i<=j){
        while(!(isalpha(ch[i]))){
            rev[i]=ch[i];
            i++;
        }
        while(!(isalpha(ch[j]))){
            rev[j]=ch[j];
            j--;
        }
        if(i==j){
            rev[i]=ch[i];
            break;
        }
        if(i<j){
            swap(rev,ch,i,j);
            i++;
            j--;
        }
    }
    cout<<"Reversed array: "<<rev<<endl;
}
