
class Solution:
    def containsDuplicate(self, a: List[int]) -> bool:
        if len(a)!=len(set(a)):
            return True
        return False
        
        



def containsDuplicate(a):
    def maxfun(a):
        m=a[0]
        for i in range(1,len(a)):
            if a[i]>m:
                m=a[i]
        return m
    m=maxfun(a)
    b=[0]*(m+1)
    for i in a:
        b[i]+=1
    for i in b:
        if i>1:
            return True
    return False
            
a=[1,2,1]
print(containsDuplicate(a))
