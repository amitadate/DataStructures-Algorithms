def countElements(arr1,arr2):
    arr1_dict={x:0 for x in arr1}
    temp=arr1[:]
    arr2.sort()
    arr1.sort()
    i=0
    for x in range(0,len(arr1)):
        if x>0:
            count=arr1_dict[arr1[x-1]]
        else:
            count=0
        while(i<len(arr2)):
            if arr2[i]<=arr1[x]:
                count+=1
                i=i+1
            else:
                break

        arr1_dict[arr1[x]]=count
    return temp,arr1_dict







if __name__ == '__main__':
    t=int(input())
    while(t>0):
        n=int(input())
        arr1=list(map(int,input().strip().split(' ')))
        arr2 = list(map(int, input().strip().split(' ')))
        arr,arr1_dict=countElements(arr1,arr2)
        for x in arr:
            print(arr1_dict[x],end=' ')
        print()
        t=t-1
