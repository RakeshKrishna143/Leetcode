'''
Engineer's Revolution
Two sum problem
'''

nums = [2,7,11,15,3]
target = 5

def twoSum(nums,target):
    map = {}
    for index,value in enumerate(nums):
        if target - value in map:
            return [map[target-value],index]
        else:
            map[value] = index
        
print(twoSum(nums, target))
