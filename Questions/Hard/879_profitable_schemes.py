from typing import List

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        num_crimes = len(group)

        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(num_crimes + 1)]

        for members in range(n + 1):
            dp[num_crimes][members][0] = 1

        for i in range(num_crimes - 1, -1, -1):
            for members in range(n + 1):
                for curr_profit in range(minProfit + 1):
                    dp[i][members][curr_profit] = dp[i + 1][members][curr_profit]

                    if group[i] <= members:
                        new_profit = max(0, curr_profit - profit[i])
                        dp[i][members][curr_profit] += dp[i + 1][members - group[i]][new_profit]

                    dp[i][members][curr_profit] %= MOD

        return dp[0][n][minProfit]
