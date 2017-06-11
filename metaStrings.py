def swapCheck(str1,str2,index):
    if(str1[index[0]]==str2[index[1]] and str1[index[1]]==str2[index[0]]):
        return True
    else:
        return False

def checkMeta(str1,str2):
    count=0
    index=[]
    if(len(str1)!=len(str2)):
        return 0
    i=0
    while(i<len(str1)):
        if str1[i]!=str2[i]:
            index.append(i)
            count=count+1
        if(count>2):
            return 0
        i=i+1
    if(count==2):
        if swapCheck(str1,str2,index):
            return 1
        else:
            return 0
    else:
        return 0




if __name__=='__main__':
    t=int(input())
    while(t!=0):
        str1=input().strip()
        str2 = input().strip()
        ans=checkMeta(str1,str2)
        print(ans)
        t=t-1
