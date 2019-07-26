a=[2,3,4,5,6,7]
target=7

def combinationalsum(a,target):
    res=[]
    dfs(a,target,0,[],res)
    return res 
    
def dfs(b,target,index,path,res):
    if target==0:
        res.append(path)
        return 
    if target<0:
        return
    for i in range(index,len(a)):
        if b[i]>target:
            break
        dfs(b,target-b[i],i,path+[b[i]],res)
        
print(combinationalsum(a,target))
    
