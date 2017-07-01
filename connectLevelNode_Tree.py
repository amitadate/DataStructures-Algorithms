import queue

class Node:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.nextRight=None
        self.data=value

def connectBt(root,q):
    newq=queue.Queue()
    node=root
    while(not q.empty()):
        if node.left:
            newq.put(node.left)
        if node.right:
            newq.put(node.right)
        nextNode=q.get()
        node.nextRight=nextNode
        node=nextNode
    if node.left:
        newq.put(node.left)
    if node.right:
        newq.put(node.right)
    if newq.empty():
        return
    else:
        return connectBt(newq.get(),newq)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def leverorder(root):
    temp=root
    if temp.nextRight:
        while(temp.nextRight!=None):
            print(temp.data,sep=' ',end=' ')
            temp=temp.nextRight
        print(temp.data)
    else:
        print(root.data)
    if root.left:
        return leverorder(root.left)
    elif(not root.left and root.right):
        return leverorder(root.right)
    else:
        return



if __name__ == '__main__':
    bt=Node(10)
    bt.left=Node(20)
    bt.right=Node(30)
    bt.left.left=Node(40)
    bt.left.right=Node(60)
    bt.right.right=Node(70)
    q=queue.Queue()
    q.put(bt)
    connectBt(q.get(),q)
    print('Level Order')
    leverorder(bt)
    print('Inorder')
    inorder(bt)
