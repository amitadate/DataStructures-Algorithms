#returns modulus of two subroutines
def mergePow(x,y,c):
    return (x*y)%c

#recurse pow(a,b)%c
def powRecurse(a,b,c):
    if b==1:
        return a%c
    mid=b//2
    x=powRecurse(a,mid,c)
    y=powRecurse(a,b-mid,c)
    z=mergePow(x,y,c)
    return z

#input
if __name__=='__main__':
    t=int(input())
    while(t!=0):
        val=list(map(int,input().strip().split()))
        a,b,c=val[0],val[1],val[2]
        ans=powRecurse(a,b,c)
        print(ans)
        t=t-1
