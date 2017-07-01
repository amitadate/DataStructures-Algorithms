class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None


def convertExp(node,stack):
    if len(stack)==0:
        return None
    item=stack.pop()
    if item==':':
        return item
    if item=='?':
        newItem=stack.pop()
        node.left=Node(newItem)
        returnedVal=convertExp(node.left,stack)
    if returnedVal==':':
        if node.right==None:
            newItem=stack.pop()
            node.right=Node(newItem)
            returnedVal=convertExp(node.right,stack)
        else:
            return returnedVal
    return returnedVal


def inorder(root):
    if root:
        print(root.data)
        inorder(root.left)
        inorder(root.right)

if __name__ == '__main__':
    stack=list(reversed(input('Enter expression').split(' ')))
    item=stack.pop()
    node=Node(item)
    convertExp(node,stack)
    inorder(node)

