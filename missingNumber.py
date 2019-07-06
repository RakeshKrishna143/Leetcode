class Solution:
    def missingNumber(self, a: List[int]) -> int:
        
        def maxfun(a):
            m=a[0]
            for i in range(1,len(a)):
                if a[i]>m:
                    m=a[i]
            return m

        m=maxfun(a)
        b=[0]*(m+1)
        for i in a:
            b[i]=1 
        print(b)
        for i in range(len(b)):
            if b[i]!=1:
                return i
        return m+1
