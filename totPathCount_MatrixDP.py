def countPath(x,y,m,n,dp):
    if x>m-1 or y>n-1:
        return 0
    if x==m-1 and y==n-1:
        return 1
    if dp[x][y]!=-1:
        return dp[x][y]
    p1=countPath(x+1,y,m,n,dp)
    p2=countPath(x,y+1,m,n,dp)
    dp[x][y]=p1+p2
    return p1+p2

if __name__ == '__main__':
    t=int(input())
    while(t>0):
        m,n=input().strip().split(' ')
        m,n=int(m),int(n)
        dp=[[-1 for x in range(n)] for x in range(m)]
        print(countPath(0,0,m,n,dp))
        t-=1
