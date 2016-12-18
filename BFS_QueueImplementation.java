import java.util.Queue;
import java.util.LinkedList;
//declaring Node structure
class Node{
    int key;
    Node left,right;
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
    //Using Queue to implement BFS
    public void BFS(Node root){
        Queue<Node> queue=new LinkedList<Node>();
        queue.add(root);
        while(!queue.isEmpty()){
            Node tempnode=queue.poll();
            System.out.print(tempnode.key+" ");
            if(tempnode.left!=null){
                queue.add(tempnode.left);
            }
            if(tempnode.right!=null){
                queue.add(tempnode.right);
            }
        }
    }
    
    public static void main(String[] args){
        BinaryTree tree=new BinaryTree();
        //building tree
        tree.root=new Node(1);
        tree.root.left=new Node(2);
        tree.root.right=new Node(3);
        tree.root.left.left=new Node(4);
        tree.root.left.right=new Node(5);
        System.out.println("BFS output:");
        tree.BFS(tree.root);
    }
}
