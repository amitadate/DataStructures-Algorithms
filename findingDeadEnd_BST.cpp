//http://www.geeksforgeeks.org/check-whether-bst-contains-dead-end-not/
#include<bits/stdc++.h>
using namespace std;

struct Node{
    int data;
    struct Node* left;
    struct Node* right;
};

struct Node *newNode(int key){
    Node *node=new Node;
    node->data=key;
    node->left=node->right=NULL;
    return node;
}

struct Node *insert(struct Node *node, int key){
    if(node==NULL){
        //returning the newly created node
        return newNode(key);
    }
    if(key<node->data){
        node->left=insert(node->left,key);
    }
    if(key>node->data){
        node->right=insert(node->right,key);
    }
    //returning the unchanged node
    return node;
}

void storeNodes(struct Node *node, unordered_set<int> &all_nodes, unordered_set<int> &leaf_nodes){
    all_nodes.insert(node->data);
    if(node->left==NULL && node->right==NULL){
        leaf_nodes.insert(node->data);
        return;
    }
    
    if(node->left){
        storeNodes(node->left,all_nodes,leaf_nodes);
    }
    if(node->right){
        storeNodes(node->right,all_nodes,leaf_nodes);
    }
}

bool deadEnd(struct Node *node){
    unordered_set<int> all_nodes,leaf_nodes;
    if(node==NULL)return false;
    //adding 0 to handle dead end for 1
    all_nodes.insert(0);
    storeNodes(node,all_nodes,leaf_nodes);
    unordered_set<int>::iterator ii;
    int count=0;
    for(ii=leaf_nodes.begin();ii!=leaf_nodes.end();++ii){
        int x=(*ii);
        if(all_nodes.find(x+1)!=all_nodes.end() && all_nodes.find(x-1)!=all_nodes.end()){
            cout<<"Dead end at :"<<x<<endl;
            count++;
        }
            
    }
    if(count>0)
        return true;
    else
        return false;
}

int main(){
    Node *root=NULL;
    root = insert(root, 8);
    root = insert(root, 7);
    root = insert(root, 10);
    root = insert(root, 2);
    root = insert(root, 9);
    root = insert(root, 13);
    //root = insert(root, 4);
    if(deadEnd(root))
        cout<<"Yes";
    else
        cout<<"No";
    return 0;
    
}
