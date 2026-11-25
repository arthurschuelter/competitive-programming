class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s = set()

        for n in nums:
            if n in s:
                return True
            s.add(n)
            
        return False

import pytest

solution = Solution()

@pytest.mark.parametrize("nums, expected", [
    ([1,2,3,1], True),
    ([1,2,3,4], False),
    ([1,1,1,3,3,4,3,2,4,2], True)
])

def test_solution(nums, expected):
    assert solution.containsDuplicate(nums) == expected
