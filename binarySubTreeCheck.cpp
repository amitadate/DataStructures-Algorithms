//http://www.geeksforgeeks.org/check-binary-tree-subtree-another-binary-tree-set-2/
#include<bits/stdc++.h>
using namespace std;

struct Node{
    char data;
    Node *left,*right;
};

Node *newNode(int data){
    Node *node=new Node;
    node->data=data;
    node->left=node->right=NULL;
}

bool traversal(Node*T, Node *S){
    if(!(T->data==S->data)){
        return false;
    }
    if((T->left!=NULL &&S->left==NULL)||(T->right!=NULL &&S->right==NULL)){
        return false;
    }
    if(T->left!=NULL && S->left!=NULL){
        bool check=traversal(T->left,S->left);
        if(check==false)return false;
    }
    if(T->right!=NULL && S->right!=NULL){
        bool check=traversal(T->right,S->right);
        if(check==false)return false;
    }
    return true;
}

bool isSubtree(Node* T,Node *S){
    if(S->data==T->data){
       bool check=traversal(T,S); 
       if(check==true)return true;
    }
    if(T->left!=NULL){
        isSubtree(T->left,S);
    }
    if(T->right!=NULL){
        isSubtree(T->right,S);
    }
    return false;
}

int main(){
    Node *T = newNode('a');
    T->left = newNode('b');
    T->right = newNode('d');
    T->left->left = newNode('c');
    T->right->right = newNode('e');
 
    Node *S = newNode('a');
    S->left = newNode('b');
    S->left->left = newNode('c');
    S->right = newNode('d');
 
    if (isSubtree(T, S))
        cout << "Yes: S is a subtree of T";
    else
        cout << "No: S is NOT a subtree of T";
 
    return 0;
}
