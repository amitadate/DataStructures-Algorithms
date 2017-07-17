def lcs(str1,sr2,m,n,mem):
    if m<0 or n<0:
        return 0
    if mem[m][n]!=None:
        return mem[m][n]
    if str1[m]==str2[n]:
        sol=1+lcs(str1,str2,m-1,n-1,mem)
        mem[m][n]=sol
        return sol
    else:
        sol= max(lcs(str1,str2,m-1,n,mem),lcs(str1,str2,m,n-1,mem))
        mem[m][n]=sol
        return sol

if __name__ == '__main__':
    str1=input().strip()
    str2=input().strip()
    mem=[[None for x in range(len(str2))]for y in range(len(str1))]
    sol=lcs(str1,str2,len(str1)-1,len(str2)-1,mem)
    print(sol)
