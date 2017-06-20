import math

def toString(arr):
    return ' '.join(str(x) for x in arr)

def checkFibo(x):
    m1=5*math.pow(x,2)+4
    m2=5*math.pow(x,2)-4
    if(m1>=0):
        c1=math.sqrt(m1)
    if(m2>=0):
        c2=math.sqrt(m2)
    if c1-int(c1)==0 or c2-int(c2)==0:
        return True
    else:
        return False

def largestSub(arr):
    ans=[]
    flag=False
    for i in range(0,len(arr)):
        flag=checkFibo(arr[i])
        if(flag):
            ans.append(arr[i])
        flag=False
    return ans

if __name__ == '__main__':
    t=int(input())
    while(t!=0):
        n=int(input())
        arr=list(map(int,input().strip().split(' ')))
        ans=largestSub(arr)
        print(toString(ans))
        #print(ans)
        t=t-1
