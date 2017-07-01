import queue

class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

class BST:
    def __init__(self):
        self.root=None

    def insert(self,data,root):
        if data<=root.data:
            if root.left==None:
                root.left=Node(data)
            else:
                self.insert(data,root.left)
        else:
            if root.right==None:
                root.right=Node(data)
            else:
                self.insert(data,root.right)

    def levelOrder(self,root):
        q=queue.Queue()
        q.put(root)
        while(not q.empty()):
            node=q.get()
            print(node.data)
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)

    def bstRange(self,root,x,y,l):
        if root==None:
            return 0
        if root.data<x:
            countR=self.bstRange(root.right,x,y,l)
            return countR
        elif root.data>y:
            countL=self.bstRange(root.left,x,y,l)
            return countL
        else:
            l.append(root.data)
            countR=self.bstRange(root.right,x,y,l)
            countL = self.bstRange(root.left, x, y,l)
            return 1+countL+countR


if __name__ == '__main__':
    bst=BST()
    bst.root=Node(10)
    bst.insert(5,bst.root)
    bst.insert(50,bst.root)
    bst.insert(1,bst.root)
    bst.insert(40,bst.root)
    bst.insert(100,bst.root)
    bst.levelOrder(bst.root)
    l=[]
    ans=bst.bstRange(bst.root,5,45,l)
    print('tot nodes in range are: ',ans,l)
