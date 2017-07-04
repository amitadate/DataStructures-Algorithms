#http://practice.geeksforgeeks.org/problems/find-the-odd-occurence/0

def printOdd(hmap):
    for x in hmap:
        if hmap[x]%2!=0:
            print(x,'',end='')
    print()

def findOdd(arr):
    hmap={}
    for x in arr:
        if x in hmap:
            hmap[x]=hmap[x]+1
        else:
            hmap[x]=1
    return hmap

if __name__ == '__main__':
    t=int(input())
    while(t>0):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        hmap=findOdd(arr)
        printOdd(hmap)
        t-=1
