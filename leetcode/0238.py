from typing import List
class Solution:
    # Time: O(n^2)
    # Space: O(n + n) => O(n)
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     mults = [1 for n in nums]

    #     for i in range(len(nums)):
    #         for j in range(len(nums)):
    #             if i == j:
    #                 continue
    #             mults[i] *= nums[j]

    #     return mults
    

    # Time: O(n)
    # Space: O(n + n + n) => O(n)

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        hasZero = 0
        p = 1
        for n in nums:
            if (n == 0):
                hasZero += 1
                continue
            p *= n
        
        if hasZero > 1:
            return [0] * len(nums)

        ans = [p] * len(nums)
        for i in range(len(nums)):
            if hasZero == 0:
                ans[i] = ans[i] // nums[i]
            elif hasZero == 1 and nums[i] != 0:
                ans[i] = 0
            else:
                ans[i] = p
            

        return ans


import pytest

solution = Solution()

@pytest.mark.parametrize("nums, expected", [
    ([1,2,3,4], [24,12,8,6]),
    ([-1,1,0,-3,3], [0,0,9,0,0]),
])

def test_solution(nums, expected):
    assert sorted(solution.productExceptSelf(nums)) == sorted(expected)
