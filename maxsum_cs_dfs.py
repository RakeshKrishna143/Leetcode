def maxsum(b):
    b[1]=max(b[0],b[1])
    for i in range(2,len(b)):
        b[i]=max(b[i-1],a[i]+b[i-2])
    return b[-1]

def cs(a,target):
    res=[]
    dfs(a,target,0,[],res)
    return res 
    
def dfs(a,target,index,path,res):
    if target==0:
        res.append(path)
        return
    elif target<0:
        return
    else:
        for i in range(index,len(a)):
            dfs(a,target-a[i],i+2,path+[a[i]],res)
    return res
a=[1,3,3,1,2,5,5,2]
b=a.copy()
print(cs(a,maxsum(b)))

