class Solution:
    def mincostTickets(self, days: 'List[int]', costs: 'List[int]') -> 'int':
        dp = [0]*(max(days)+1)
        j = 0
        for i in range(days[0], (max(days)+1)):
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
                    return dp[-1]
            else:
                if i > 0:
                    dp[i] = dp[i-1]
