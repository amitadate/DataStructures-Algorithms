def quickSort(arr,l,r):
    if l>=r:
        return
    pivot=arr[l]
    i=l
    j=l+1
    while(i<=r and j<=r):
        if arr[j]<pivot:
            arr[i+1],arr[j]=arr[j],arr[i+1]
            i+=1
            j+=1
        else:
            j+=1
    arr[l],arr[i]=arr[i],arr[l]
    quickSort(arr,l,i-1)
    quickSort(arr,i+1,r)



if __name__ == '__main__':
    arr=list(map(int,input().strip().split(' ')))
    quickSort(arr,0,len(arr)-1)
    print(arr)
