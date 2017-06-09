#count split inversions (while merging)
def splitInv(arr,ini,mid,fi):
    len_b=mid-ini+1
    split=0
    rem_b=len_b
    len_c=fi-(mid+1)+1
    i=0
    j=0
    k=ini
    arr_b=arr[ini:mid+1]
    arr_c=arr[mid+1:fi+1]
    while(i<len_b and j<len_c):
        if arr_b[i]<=arr_c[j]:
            arr[k]=arr_b[i]
            k=k+1
            i=i+1
            rem_b=rem_b-1
        elif arr_b[i]>arr_c[j]:
            arr[k]=arr_c[j]
            k=k+1
            j=j+1
            split=split+rem_b

    while(i<len_b):
        arr[k]=arr_b[i]
        k=k+1
        i=i+1
    while (j<len_c):
        arr[k] = arr_c[j]
        k = k + 1
        j = j + 1
    return split

#recursive routine
def countInv(arr,ini,fi):
    if ini==fi:
        return 0
    mid=(ini+fi)//2
    x=countInv(arr,ini,mid)
    y=countInv(arr,mid+1,fi)
    z=splitInv(arr,ini,mid,fi)
    return (x+y+z)

#accept array
if __name__=='__main__':
    arr=list(map(int,input('Enter Array: ').strip().split(' ')))
    totInversions=countInv(arr,0,len(arr)-1)
    print('Sorted Array: ',arr)
    print('Total Inversions: ',totInversions)
