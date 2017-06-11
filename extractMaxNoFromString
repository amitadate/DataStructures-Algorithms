#http://practice.geeksforgeeks.org/problems/extract-maximum/0

import re

#returns max no in string through linear scan
def find_max(str):
    max_val=0
    p=re.compile('(\d+)')
    iterator=p.finditer(str)
    for match in iterator:
        val=int(match.group())
        if val>max_val:
            max_val=val

    return max_val




#input
if __name__=='__main__':
    t=int(input())
    while(t!=0):
        str=input().strip()
        max_no=find_max(str)
        print(max_no)
        t=t-1
