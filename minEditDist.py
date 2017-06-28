def minEdit(str1,str2,m,n):
    if m<0 and n<0:
        return 0
    if m<0:
        return n+1
    if n<0:
        return m+1
    if str1[m]==str2[n]:
        return minEdit(str1,str2,m-1,n-1)
    else:
        return 1+min(minEdit(str1,str2,m-1,n-1),
                     minEdit(str1,str2,m,n-1),
                     minEdit(str1,str2,m-1,n))




if __name__ == '__main__':
    str1=input('Enter string 1')
    str2=input('Enter string 2')
    m=len(str1)-1
    n=len(str2)-1
    totSteps=minEdit(str1,str2,m,n)
    print(totSteps)
