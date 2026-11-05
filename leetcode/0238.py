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
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_mult, r_mult = 1, 1
        n = len(nums)
        l_arr = [0] * n
        r_arr = [0] * n

        for i in range(n):
            j = n - i -1

            l_arr[i] = l_mult
            l_mult *= nums[i]

            r_arr[j] = r_mult
            r_mult *= nums[j]

        return [l * r for l, r in zip(l_arr, r_arr)]


import pytest

solution = Solution()

@pytest.mark.parametrize("nums, expected", [
    # Test case 1 
    ([1,2,3,4], [24,12,8,6]),
    # Test case 2
    ([-1,1,0,-3,3], [0,0,9,0,0]),
])

def test_solution(nums, expected):
    result = solution.productExceptSelf(nums)

    assert sorted(result) == sorted(expected)
