#http://www.geeksforgeeks.org/print-binary-tree-vertical-order-set-2/

class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

def printVertical(root,pos,index):
    if root.left:
        pos.setdefault(index-1,[]).append(root.left.data)
        printVertical(root.left,pos,index-1)
    if root.right:
        pos.setdefault(index + 1, []).append(root.right.data)
        printVertical(root.right, pos, index + 1)


if __name__ == '__main__':
    bt=Node(1)
    bt.left=Node(2)
    bt.right=Node(3)
    bt.left.left=Node(4)
    bt.left.right=Node(5)
    bt.right.left=Node(6)
    bt.right.right=Node(7)
    bt.right.left.right=Node(8)
    bt.right.right.right=Node(9)
    pos={0:[bt.data]}
    printVertical(bt,pos,0)
    order=sorted(pos.items())
    print(pos)
    for x in order:
        print(' '.join(str(y) for y in x[1]))
