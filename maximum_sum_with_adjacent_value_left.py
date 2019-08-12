#maximum sum with adjacent value left

nums=[2,1,3,1,1,9,1,1,1,1,8,1,7]
nums[1] = max(nums[0], nums[1])
        
for i in range(2, len(nums)):
    nums[i] = max(nums[i-1], nums[i] + nums[i-2])
print(nums[-1])
print(nums)
