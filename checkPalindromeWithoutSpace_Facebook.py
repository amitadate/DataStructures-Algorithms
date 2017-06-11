
def checkPalindrome(str):
    j=len(str)-1
    i=0
    flag=True
    while(i<len(str) and j>=0):
        if str[i]==' ':
            i=i+1
            continue
        elif str[j]==' ':
            j=j-1
            continue
        if str[i]!=str[j]:
            flag=False
            break
        j=j-1
        i=i+1
    if flag==True:
        return True
    else:
        return False


if __name__=="__main__":
    t=int(input())
    while(t!=0):
        str=input().strip()
        ans=checkPalindrome(str)
        if ans:
            print('YES')
        else:
            print('NO')
        t=t-1
