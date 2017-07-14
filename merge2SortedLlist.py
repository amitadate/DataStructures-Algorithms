#http://www.geeksforgeeks.org/merge-two-sorted-linked-lists/

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Llist:
    def __init__(self):
        self.head=None

    def createList(self,arr1):
        for x in arr1:
            newNode=Node(x)
            self.insert(newNode)

    def insert(self,newNode):
        if self.head==None:
            self.head=newNode
            return
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next=newNode

    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data,' ',end='')
            temp=temp.next
        print()

    def insertNode(self,prev,new):
        new.next=prev.next
        prev.next=new

def sortLlist(llist1,llist2):
        temp1=llist1.head
        temp2=llist2.head
        if temp1.data>temp2.data:
            llist1.head=temp2
            llist2.head=temp2.next
            temp2.next=temp1
            temp1=llist1.head
            temp2=llist2.head
        while(temp2 and temp1.next):
            if temp2.data<temp1.next.data:
                next2=temp2.next
                llist1.insertNode(temp1,temp2)
                temp2=next2
                temp1=temp1.next
            else:
                temp1=temp1.next

        if temp2:
            temp1.next=temp2

if __name__ == '__main__':
    t=int(input())
    while(t>0):
        m,n=input().strip().split()
        m,n=int(m),int(n)
        arr1=list(map(int,input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        llist1=Llist()
        llist1.createList(arr1)
        llist2=Llist()
        llist2.createList(arr2)
        llist1.printList()
        sortLlist(llist1,llist2)
        print('After sorting')
        llist1.printList()
        t=t-1

