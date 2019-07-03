nums=[2,7,11,15]
target=9
d={}
for i,num in enumerate(nums):
    n=target-num
    if n not in d:
        d[num]=i 
    else:
        print(d[n],i)
