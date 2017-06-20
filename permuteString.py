def toString(List):
   return ''.join(List)

#uses backtracking
def permute(arr,l,r):
    if l==r:
        print(toString(arr))
    else:
        for i in range(l,r+1):
            arr[l],arr[i]=arr[i],arr[l]
            permute(arr,l+1,r)
            arr[l],arr[i]=arr[i],arr[l]


if __name__=='__main__':
    str=input()
    permute(list(str),0,len(str)-1)
