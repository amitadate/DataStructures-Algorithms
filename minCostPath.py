#http://www.geeksforgeeks.org/dynamic-programming-set-6-min-cost-path/

def minCost(cost,m,n):
    tc=[[0 for i in range(m+1)]for j in range(n+1)]
    tc[0][0]=cost[0][0]
    #initializing row 0
    for i in range(1,n+1):
        tc[0][i]=tc[0][i-1]+cost[0][i]

    #initializing col 0
    for i in range(1,m+1):
        tc[i][0]=tc[i-1][0]+cost[i][0]

    for i in range(1,m+1):
        for j in range(1,n+1):
            tc[i][j]=min(tc[i-1][j-1],tc[i-1][j],tc[i][j-1])+cost[i][j]

    return tc

def reconstructPath(tc,cost,m,n,path):
    path.insert(0,(m,n))
    if m==0 and n==0:
        return
    if m==0:
        return reconstructPath(tc,cost,m,n-1,path)
    if n==0:
        return reconstructPath(tc,cost,m-1,n,path)
    if tc[m-1][n-1]<tc[m-1][n] and tc[m-1][n-1]<tc[m][n-1]:
        return reconstructPath(tc,cost,m-1,n-1,path)
    elif tc[m][n-1]<tc[m-1][n] and tc[m][n-1]<tc[m-1][n-1]:
        return reconstructPath(tc,cost,m,n-1,path)
    else:
        return reconstructPath(tc,cost,m-1,n,path)


if __name__ == '__main__':
    cost = [[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]
    tc=minCost(cost, 2, 2)
    path=[]
    reconstructPath(tc,cost,2,2,path)
    print(tc[2][2])
    print('->'.join(str(i) for i in path))
