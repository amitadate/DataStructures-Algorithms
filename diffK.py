# code

# checks if distinct pair
def checkPair(a,b,pairs):
    if (a,b) in pairs:
        return True
    else:
        return False

# iterates through the array
def loopArr(arr, n,k):
    tot=0
    elementSet=set()
    pairs=set()
    for i in arr:
        if i+k in elementSet:
            if not(checkPair(i,i+k,pairs)):
                pairs.add((i,i+k))
                tot=tot+1
                #print(i,i+k)
        if i-k in elementSet:
            if not(checkPair(i-k,i,pairs)):
                pairs.add((i-k,i))
                tot = tot + 1
                #print(i-k, i)
        elementSet.add(i)
    return tot






# input array
if __name__ == '__main__':
    t = int(input())
    while (t != 0):
        n = int(input())
        arr = list(map(int, input().split(' ')))
        k=int(input())
        tot=loopArr(arr, n,k)
        print(tot)
        t=t-1
