//http://www.geeksforgeeks.org/convert-string-repetition-substring-k-length/
#include<bits/stdc++.h>
using namespace std;

bool check(string ch,int k){
    map<string,int> mp;
    map<string,int>::iterator itr;
    
    int i;
    int n=ch.length();
    
    if(n%k!=0){
        return false;
    }
    //Store elements in the Map
    for(i=0;i<n;i+=k){
        mp[ch.substr(i,k)]++;
    }
    
    //Print elements of the Map
    cout<<"Elements of the Map :"<<endl;
    for(itr=mp.begin();itr!=mp.end();++itr){
        cout<<itr->first<<" "<<itr->second<<endl;
    }
    
    if(mp.size()==1){
        cout<<"No conversion of srings needed, only repeating patterns\n";
        return true;
    }
    
    if(mp.size()>2){
        cout<<"Too many sub-patterns\n";
        return false;
    }
    
    if(mp.size()==2){
        if(mp.begin()->second==1 || mp.begin()->second==(n/k-1))return true;
        else return  false;
    }
}


int main(){
    string ch="abcdef";
    int k=2;
    check(ch,k)?cout<<"Yes":cout<<"No";
    return 0;
}
