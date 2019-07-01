class Solution:
    def twoSum(self, a: List[int], s: int) -> List[int]:
        for i in range(len(a)-1):
            for j in range(i+1,len(a)):
                if a[i]+a[j]==s:
                    break
            else:
                continue
            break
        return [i,j]
