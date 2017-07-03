def findMax(arr,maxSoFar,curr):
    for i in range(1,len(arr)):
        curr=max(arr[i],curr+arr[i])
        maxSoFar=max(maxSoFar,curr)
    return maxSoFar

if __name__ == '__main__':
    t=int(input())
    while(t>0):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        maxSoFar,curr=arr[0],arr[0]
        print(findMax(arr,maxSoFar,curr))
        t-=1
