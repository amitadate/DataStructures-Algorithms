import sys

class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

def printSum(root,strList):
    strList.append(root.data)
    if root.left==None and root.right==None:
        return ''.join(str(x) for x in strList)
    if root.left:
        sum1=printSum(root.left,strList[:])
    else:
        sum1=0
    if root.right:
        sum2=printSum(root.right,strList[:])
    else:
        sum2=0
    return int(sum1)+int(sum2)

def minDepth(root,level):
    if root.left==None and root.right==None:
        return level
    if root.left:
        dL=minDepth(root.left,level+1)
    else:
        dL=sys.maxsize
    if root.right:
        dR=minDepth(root.right,level+1)
    else:
        dR=sys.maxsize
    return min(dL,dR)




if __name__ == '__main__':
    bt=Node(10)
    bt.left=Node(20)
    bt.right=Node(30)
    bt.left.left=Node(40)
    bt.left.right=Node(60)
    bt.left.right.left=Node(7)
    bt.left.right.right = Node(4)
    bt.right.right=Node(4)
    strList=[]
    #sumTot=printSum(bt,strList)
    minDP=minDepth(bt,1)
    #print(sumTot)
    print(minDP)
