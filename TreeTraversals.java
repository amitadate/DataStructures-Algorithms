class Node{
    int key;
    Node left, right;
    Node(int data){
        key=data;
        left=right=null;
    }
}

class BinaryTree{
    Node root;
    BinaryTree(){
        root=null;
        
    }
    
    void printInorder(Node node){
        if(node==null){
            return;
        }
        printInorder(node.left);
        System.out.print(node.key+" ");
        printInorder(node.right);
        
    }
    
    void printPostorder(Node node){
        if(node==null){
            return;
        }
        printPostorder(node.left);
        printPostorder(node.right);
        System.out.print(node.key+" ");
    }
    
    void printPreorder(Node node){
        if(node==null){
            return;
        }
        System.out.print(node.key+" ");
        printPreorder(node.left);
        printPreorder(node.right);
        
    }
    
    public static void main(String[] args){
        BinaryTree tree=new BinaryTree();
        tree.root=new Node(1);
        tree.root.left=new Node(2);
        tree.root.right=new Node(3);
        tree.root.left.left=new Node(4);
        tree.root.left.right=new Node(5);
        
        System.out.println("\nInorder");
        tree.printInorder(tree.root);
        System.out.println("\nPreorder");
        tree.printPreorder(tree.root);
        System.out.println("\nPostorder");
        tree.printPostorder(tree.root);
    }
    
}
