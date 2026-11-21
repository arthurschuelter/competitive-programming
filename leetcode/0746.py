class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        dp = [0] * (n+1)

        for i in range(n-1, -1, -1):
            dp[i] = dp[i+1] + cost[i]
            if i + 2 <= n:
                dp[i] = min(dp[i+2] + cost[i], dp[i])
            
        return min(dp[0], dp[1])
        

import pytest

solution = Solution()
@pytest.mark.parametrize("cost, expected", [
    ([10,15,20], 15),
    ([1,100,1,1,1,100,1,1,100,1], 6),
])

def test_solution(cost, expected):
    assert solution.minCostClimbingStairs(cost) == expected