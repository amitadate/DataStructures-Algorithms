class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        newNode=Node(data)
        temp=self.head
        if(temp==None):
            self.head=newNode
            return
        while(temp.next):
            temp=temp.next
        temp.next=newNode

    def print(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

    def delete(self,prev,temp):
        prev.next=temp.next
        temp=None

    def removeDup(self):
        s=set()
        temp=self.head
        prev=None
        while(temp):
            if s.__contains__(temp.data):
                t=temp.next
                self.delete(prev,temp)
                temp=t
            else:
                s.add(temp.data)
                prev=temp
                temp=temp.next


if __name__ == '__main__':
    llist=LinkedList()
    llist.append('F')
    llist.append('O')
    llist.append('L')
    llist.append('L')
    llist.append('O')
    llist.append('W')
    llist.append(' ')
    llist.append('U')
    llist.append('P')
    print('Original')
    llist.print()
    print('After removing duplicates')
    llist.removeDup()
    llist.print()

