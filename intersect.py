#Counter
from collections import Counter
class Solution:
    def intersect(self, a1: List[int], a2: List[int]) -> List[int]:
        d=Counter(a1)&Counter(a2)
        l=[]
        for i in d:
            j=d[i]
            while j>0:
                l.append(i)
                j-=1
        return l
                
#list
from collections import Counter
class Solution:
    def intersect(self, a1: List[int], a2: List[int]) -> List[int]:
        b=[]              
        for i in a1:
            if i in a2:
                b.append(i)
                a2.remove(i)
        return b

#count sort
class Solution:
    def intersect(self, a1: List[int], a2: List[int]) -> List[int]:
        if len(a1)==0:
            return a1
        if len(a2)==0:
            return a2
        def maxfun(a):
            m=a[0]
            for i in range(len(a)):
                if a[i]>m:
                    m=a[i]
            return m
        
        m1=maxfun(a1)
        m2=maxfun(a2)
        m=min(m1,m2)
        b=[0]*(m+1)
        for i in a1:
            if i<=m:
                b[i]+=1
        
        c=[]
        for i in a2:
            if i<len(b) and b[i]>=1:
                c.append(i)
                b[i]-=1
        return c
