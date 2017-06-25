class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Llist:
    def __init__(self):
        self.head=None

    def append(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            return

        temp=self.head
        while(temp.next):
            temp=temp.next

        temp.next=newNode

    def print(self):
        temp=self.head
        while(temp):
            print(temp.data,'->',end='')
            temp=temp.next
        print('NULL\n')

    def reverseUtil(self,curr,prev):
        if curr.next==None:
            self.head=curr
            curr.next=prev
            return

        next=curr.next
        curr.next=prev
        self.reverseUtil(next,curr)

    def reverse(self):
        if self.head==None:
            return
        self.reverseUtil(self.head,None)



if __name__ == '__main__':
    llist=Llist()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.print()
    llist.reverse()
    llist.print()
