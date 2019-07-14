class Solution:
    def maxProduct(self, a: List[int]) -> int:
        b=a[::-1]
        for i in range(1,len(a)):
            a[i]*=a[i-1] or 1
            b[i]*=b[i-1] or 1
        return max(a+b)
        
        
