from heapq import heappush,heappop,heapreplace

class Heap:
    def __init__(self,k):
        self.heapList=[]
        self.size=0
        self.maxSize=k

    def insertC(self,key):
        if self.size<self.maxSize:
            heappush(self.heapList,key)
            self.size+=1
            return
        if self.heapList[0]>=key:
            return
        heapreplace(self.heapList,key)

    def kthLargest(self):
        if self.size<k:
            return -1
        else:
            self.size-=1
            return heappop(self.heapList)

if __name__ == '__main__':
    t=int(input())
    while t>0:
        k,n=input().strip().split(' ')
        k,n=int(k),int(n)
        heap=Heap(k)
        stream=list(map(int,input().strip().split(' ')))
        while len(stream)!=0:
            heap.insertC(stream.pop(0))
            print(heap.kthLargest(),end=' ')
        t-=1
