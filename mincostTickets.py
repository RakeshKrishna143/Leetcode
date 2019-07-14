
def mincostTickets(days,costs):
    dp = [0]*366
    j = 0
    for i in range(days[0], 366):
        if i == days[j]:
            dp[i] = dp[i-1]+costs[0]
            if i >= 7:
                dp[i] = min(dp[i],dp[i-7]+costs[1])
            else:
                dp[i] = min(dp[i], costs[1])
            if i >= 30:
                dp[i] = min(dp[i],dp[i-30]+costs[2])
            else:
                dp[i] = min(dp[i], costs[2])
            j += 1
            if j == len(days):
                return dp[i]
        else:
            if i > 0:
                dp[i] = dp[i-1]
days = [1,4,6,7,8,20]
costs = [2,7,15]                
print(mincostTickets(days,costs))
