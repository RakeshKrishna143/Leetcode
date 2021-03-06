class Solution:
    def threeSum(self, nums):
        solution = []
        length = len(nums)-1
        nums.sort()                            

        for i in range(length-1):
            if i > 0 and nums[i] == nums[i-1]: 
                continue
            j = i+1
            k = length
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if not temp:
                    solution.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif temp < 0:
                    j += 1
                else:
                    k -= 1
        return solution
