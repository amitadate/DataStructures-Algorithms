#http://www.geeksforgeeks.org/dynamic-programming-set-12-longest-palindromic-subsequence/

def lps(str1,m,n,mem):
    if mem[m][n]!=None:
        return mem[m][n]
    if m==n:
        sol=1
        mem[m][n]=sol
        return sol
    if str1[m]==str1[n]:
        sol=2+lps(str1,m+1,n-1,mem)
        mem[m][n]=sol
        return sol
    else:
        sol=max(lps(str1,m+1,n,mem),lps(str1,m,n-1,mem))
        mem[m][n]=sol
        return sol

if __name__ == '__main__':
    str1=input().strip()
    m=len(str1)
    mem=[[None for i in range(m)]for j in range(m)]
    sol=lps(str1,0,m-1,mem)
    print(sol)
