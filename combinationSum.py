def combinationSum(candidates, target):
    res = []
    candidates.sort()
    dfs(candidates, target, 0, [], res)
    return res
    
def dfs(nums, target, index, path, res):
    if target < 0:
        return  
    if target == 0:
        res.append(path)
        return 
    for i in range(index, len(nums)):
        if nums[i] > target:  #here  
            break
        dfs(nums, target-nums[i], i, path+[nums[i]], res)

target = 50

candidates = [i for i in range(2,target+1)]

print(combinationSum(candidates,target))
