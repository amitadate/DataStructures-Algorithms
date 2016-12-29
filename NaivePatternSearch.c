#include<stdio.h>
#include<string.h>

void search(char *text, char *pattern){
    int N=strlen(text);
    int M=strlen(pattern);
    int i;
    for(i=0;i<N-M+1;i++){
        int j;
        for(j=0;j<M;j++){
            if(text[i+j]!=pattern[j]){
                break;
                }
            }
            if(j==M){
                printf("\nPattern matched at index %d",i);
                }
        }
    
    }
    
int main(){
    char text[]="AABAACAADAABAAABAA";
    char pattern[]="AABA";
    search(text,pattern);
    return 0;
    }
