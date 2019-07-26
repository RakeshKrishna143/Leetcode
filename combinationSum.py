def combinationSum(candidates, target):
    res = []
    candidates.sort()
    dfs(candidates, target, 0, [], res)
    return res
    
def dfs(nums, target, index, path, res):
    if target < 0:
        return  # backtracking
    if target == 0:
        res.append(path)
        return 
    for i in range(index, len(nums)):
        if nums[i] > target:  #here  
            break
        dfs(nums, target-nums[i], i, path+[nums[i]], res)
candidates = [2,3,4,5,6,7]
target = 7
print(combinationSum(candidates,target))
