#every char can be kept or removed...using this concept creates all possible combinations of any size
def removeChar(str,val,flag,sol,index):
    if val.__contains__(str):
        sol.append(str)
    if index==len(str):
        return
    removeChar(str,val,False,sol,index+1)
    removeChar(str[:index]+str[index+1:],val,False,sol,index)

    if(flag==True):
        return max(sol,key=len)

#input
if __name__=='__main__':
    t=int(input())
    while(t!=0):
        n=int(input())
        val=set()
        for i in input().strip().split(' '):
            val.add(i)
        str=input().strip()
        sol=[]
        sol=removeChar(str,val,True,sol,0)
        print(sol)
        t=t-1

