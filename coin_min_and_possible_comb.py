coins=[1,2,5]
amount=11

dp=[0]+[float('inf')]*amount

for coin in coins:
    for i in range(coin,amount+1):
        dp[i]=min(dp[i],dp[i-coin]+1)
        
print(dp[-1])

d={0:1}
for  coin in coins:
    for i in range(coin,amount+1):
        d[i]=d.get(i,0)+d.get(i-coin,0)
        
print(d[amount])
        
