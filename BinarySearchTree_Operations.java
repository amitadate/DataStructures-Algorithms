class BinarySearchTree{
    class Node{
        int key;
        Node left, right;
        Node(int data){
            key=data;
            left=right=null;
        }
    }
    Node root;
    BinarySearchTree(){
        root=null;
    }
    void insert(int key){
        root=insertRec(this.root,key);
    }
    Node insertRec(Node root, int key){
        if(root==null){
            root=new Node(key);
            return root;
        }
        if(key<root.key){
            root.left=insertRec(root.left,key);
        }
        if(key>root.key){
            root.right=insertRec(root.right,key);
        }
        return root;
    }
    void inorder(){
        inorderRec(this.root);
    }
    void inorderRec(Node root){
        if(root!=null){
            inorderRec(root.left);
            System.out.print(root.key+" ");
            inorderRec(root.right);
        }
    }
    Node search(Node root, int key){
        if(root==null || root.key==key){
            return root;
        }
        if(key<root.key){
            return search(root.left,key);
        }
        if(key>root.key){
            return search(root.right,key);
        }
        return null;
    }
    public static void main (String[] args) {
        BinarySearchTree tree=new BinarySearchTree();
        tree.insert(50);
        tree.insert(30);
        tree.insert(20);
        tree.insert(40);
        tree.insert(70);
        tree.insert(60);
        tree.insert(80);
        tree.inorder();
        System.out.print("\nSearching for 90");
        Node r=tree.search(tree.root,90);
        if(r==null){
            System.out.print("\nNot found");
        }
        else{
            System.out.print("\nFound");
        }
    }
}
