#http://practice.geeksforgeeks.org/problems/unique-numbers/0

def checkDup(arr):
    h=set()
    flag=False
    for x in arr:
        if x in h:
            flag=True
            break
        h.add(x)
    return flag

def countNos(x,y):
    for n in range(x,y+1):
        arr=[int(d) for d in str(n)]
        dup=checkDup(arr)
        if(not dup):
            print(n,' ',end='')


if __name__ == '__main__':
    t=int(input())
    while(t>0):
        x,y=input().strip().split()
        x,y=int(x),int(y)
        countNos(x,y)
        t-=1
